# Import the required libraries
import gspread
import fet
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope of the Google Sheets API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# Set the path to your credentials file
creds = ServiceAccountCredentials.from_credentials.json('creds.json', scope)

# Authenticate with Google Sheets
client = gspread.authorize(creds)

# Open the Google Sheet containing the contact information
sheet = client.open('https://docs.google.com/spreadsheets/d/1Ozhr8DX-P7rchqbkMH5S-KaIk5vKTbrQg1m2kunuRPA/edit?usp=sharing').sheet1

# Add a new row to the Google Sheet with the contact information
row = ["What is your Name", "Mobile Number:", "Email Address"]  # Replace with the actual contact information
sheet.append_row(row)

  