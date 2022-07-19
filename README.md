# DIVVY - DIVIDE EXPENSES BETWEEN TWO PEOPLE

My journey of creating a project that will divide expenses between co-parents, roommates, or anyone you need to split costs with over a longer period of time.


## CONTENT

- [DIVVY - DIVIDE EXPENSES BETWEEN TWO PEOPLE](#divvy---divide-expenses-between-two-people)
  - [CONTENT](#content)
  - [REQUIREMENTS](#requirements)
  - [USAGE](#usage)

<br/>

## REQUIREMENTS

- Python 3.6+
- [Required Libraries](requirements.txt)
- Shared Google Sheet
- Google Service Account
  - Google Sheets API
  - Google Drive API
  - JSON file with your credentials - make sure your JSON file and your divvy.py file are stored in the same folder so that it is easy to link them in your code.

<br/>

## USAGE

1. Clone this repository:

   ```console
   $ git clone [https://github.com/Angamid/divvy.git] 
   # or you can download the zip file and unzip it.
   ```
   
2. Create Google Service Account
    - This is the link that I used to create a google service account
      - https://www.analyticsvidhya.com/blog/2020/07/read-and-update-google-spreadsheets-with-python/
    - You also will need to download a JSON file from the "keys" part of your service account so that you can link the code to that file in order to gain access to your shared google sheet.

3. Install required libraries:

   ```console
   $ pip install pandas
   $ pip3 install gspread
   $ pip3 install --upgrade google-api-python-client oauth2client
   ```
4. Don't forget to input your own:
    - name of JSON file in get_sheet_data() function (line 25)
    - name of google sheet in get_sheet_data() function (line 27)
    - full path to your desired folder you want the PDFs saved to (line 85)
    - text you want written in your PDF in the create_pdf(output) function (lines 90 and 106)
    - message_content in the send_email(file_name) function (line 112)
    - sender, password, and receiver in the send_email(file_name) function (lines 117-119)
        - You may need to create an APP Password from your Google email account in order for this program to login to your account and send the email.

4. Example usage:

    - `divvy.py`

      ```console
      $ python divvy.py
      ```

<br/>
