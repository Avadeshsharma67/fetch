import gspread
from oauth2client.service_account import ServiceAccountCredentials
from twilio.rest import Client

# Authenticate with Google Sheets
scope = ['https://www.googleapis.com/auth/spreadsheets.readonly']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheet containing the contact information
sheet = client.open('SubodhNotifier').sheet1

# Retrieve the contact information from the Google Sheet
contacts = sheet.get_all_records()

# Connect to Twilio API
account_sid = 'ACc15ee95abce28e2e8cd74b63b83621b0'
auth_token = '903c37caa2c2a385bdfc7ad09baecd1a'
client_twilio = Client(account_sid, auth_token)

# Define message content
data = "Hello, this is a test message Send By Avadesh Sharma!"

# Send a message to each contact
for contact in contacts:
    message = client_twilio.messages.create(
        body=data,
        from_='whatsapp:+14155238886',
        to='whatsapp:{}'.format(contact['Phone'])
    )
    print(message.sid)





"""
BEFORE RUNNING:
---------------
1. If not already done, enable the Google Sheets API
   and check the quota for your project at
   https://console.developers.google.com/apis/api/sheets
2. Install the Python client library for Google APIs by running
   `pip install --upgrade google-api-python-client`
"""
from pprint import pprint

from googleapiclient import discovery

# TODO: Change placeholder below to generate authentication credentials. See
# https://developers.google.com/sheets/quickstart/python#step_3_set_up_the_sample
#
# Authorize using one of the following scopes:
#     'https://www.googleapis.com/auth/drive'
#     'https://www.googleapis.com/auth/drive.file'
#     'https://www.googleapis.com/auth/drive.readonly'
#     'https://www.googleapis.com/auth/spreadsheets'
#     'https://www.googleapis.com/auth/spreadsheets.readonly'
credentials = None

service = discovery.build('sheets', 'v4', credentials=credentials)

# The ID of the spreadsheet to retrieve data from.
spreadsheet_id = 'my-spreadsheet-id'  # TODO: Update placeholder value.

# The A1 notation of the values to retrieve.
range_ = 'my-range'  # TODO: Update placeholder value.

# How values should be represented in the output.
# The default render option is ValueRenderOption.FORMATTED_VALUE.
value_render_option = ''  # TODO: Update placeholder value.

# How dates, times, and durations should be represented in the output.
# This is ignored if value_render_option is
# FORMATTED_VALUE.
# The default dateTime render option is [DateTimeRenderOption.SERIAL_NUMBER].
date_time_render_option = ''  # TODO: Update placeholder value.

request = service.spreadsheets().values().get(spreadsheetId='https://docs.google.com/spreadsheets/d/1Ozhr8DX-P7rchqbkMH5S-KaIk5vKTbrQg1m2kunuRPA/edit?usp=sharing', range=range_, valueRenderOption=value_render_option, dateTimeRenderOption=date_time_render_option)
response = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(response)