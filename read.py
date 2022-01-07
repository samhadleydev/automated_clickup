from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1oMB0BloDPW06u7b3xKlwwpSQn8yzkWpzUqSbKOLvm5g'

service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range="sales!A2:C2").execute()
values = result.get('values', [])

new_data = [["Zaphod", "04/01/2021", "13:00"], ["Dirk", "05/01/2021", "14:00"], ["Yak","06/01/2021", "15:00"]]

request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                                    range="sales!A5", valueInputOption="USER_ENTERED", body={"values":new_data}).execute()

print(request)