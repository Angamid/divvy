import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from fpdf import FPDF
from datetime import date
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def main():
    df = get_sheet_data()
    names = get_names(df)
    total_sum = sum_of_cost(names)
    owes = who_owes(total_sum)
    pdf = create_pdf(owes)
    send_email(pdf)

    
def get_sheet_data():

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('<INSERT_JSON_FILE_NAME_HERE>', scope)
    client = gspread.authorize(creds)
    sheet = client.open('<INSERT_GOOGLE_SHEET_NAME_HERE>')
    sheet_instance = sheet.get_worksheet(0)
    df = pd.DataFrame(sheet_instance.get_all_records())
    return df


def get_names(df):
    """This function will extract the names of the two people who need to share expenses"""
    # Have regex pull out the names of whoever is in the list in order to make sure the input names match.
    new_list = []
    result = df['Name'].str.extract(r'([A-Z][a-z]*)')
    # get the values out of the dataframe
    vals = result.values
    # add those values into a list of lists, each list a single name instance.
    name_list = vals.tolist()
    # extract each list instance of the name to make a flat list of the names.
    for name in name_list:
        for n in name:
            new_list.append(n)
    # make the list into a set so that it removes all repeats and leaves you with the two names you need.
    name_set = set(new_list)
    print(name_set)
    p_one, p_two = name_set
    return p_one, p_two, df


def sum_of_cost(names_tuple):
    """This function adds up the total each person spent based on their name and if it is an item that needs to be included in the total."""
    p_one, p_two, df = names_tuple
    # get the total spent per person from the dataframe.
    total_one = df[(df['Name']==p_one) & (df['Add to total']=='Yes')]['Cost'].sum()
    total_two = df[(df['Name']==p_two) & (df['Add to total']=='Yes')]['Cost'].sum()
    items_one = df[(df['Name']==p_one)][['Item', 'Cost']]
    items_two = df[(df['Name']==p_two)][['Item', 'Cost']]
    print(items_one.to_string())
    print(items_two.to_string())
    # split the string of costs into a list
    list_total_one = total_one.split('$')
    list_total_two = total_two.split('$')
    list_total_one.remove('')
    list_total_two.remove('')
    # add the sum of items for each person.
    total_cost_one = sum(float(sub) for sub in list_total_one)
    total_cost_two = sum(float(sub) for sub in list_total_two)
    print(total_cost_one, total_cost_two)
    # return a tuple of first sum, second sum, person one, and person two
    return total_cost_one, total_cost_two, p_one, p_two, items_one.to_string(header=None, index=False), items_two.to_string(header=None, index=False)
    
if __name__ == '__main__':
  main()
