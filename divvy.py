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
    
if __name__ == '__main__':
  main()
