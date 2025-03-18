import datetime
import os.path
import base64
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.app.created"]
TIMEZONE = "Europe/Warsaw"

def createService():
  ecred="eyJpbnN0YWxsZWQiOnsiY2xpZW50X2lkIjoiMjY2Nzg1NDIwMzY3LTIyNWc3aWNrNXE2NXJqZDBpMzJiNDl0ZHM3b3A5NmFiLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwicHJvamVjdF9pZCI6ImNsYXNzMmNhbCIsImF1dGhfdXJpIjoiaHR0cHM6Ly9hY2NvdW50cy5nb29nbGUuY29tL28vb2F1dGgyL2F1dGgiLCJ0b2tlbl91cmkiOiJodHRwczovL29hdXRoMi5nb29nbGVhcGlzLmNvbS90b2tlbiIsImF1dGhfcHJvdmlkZXJfeDUwOV9jZXJ0X3VybCI6Imh0dHBzOi8vd3d3Lmdvb2dsZWFwaXMuY29tL29hdXRoMi92MS9jZXJ0cyIsImNsaWVudF9zZWNyZXQiOiJHT0NTUFgtZkVwYkUwRnFpU3hGTWlUXzhJdmR1UGFaOW5MSSIsInJlZGlyZWN0X3VyaXMiOlsiaHR0cDovL2xvY2FsaG9zdCJdfX0="
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      decred=base64.b64decode(ecred).decode("utf-8")
      decred=json.loads(decred)
      flow = InstalledAppFlow.from_client_config(
          decred, SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("calendar", "v3", credentials=creds)
    return service
  except HttpError as error:
    print(f"An error occurred: {error}")
    return None

def createCalendar(service):
  calendar = {
    "summary": "Plan zajęć",
    "timeZone": "Europe/Warsaw",
  }

  created_calendar = service.calendars().insert(body=calendar).execute()
  print(f"Created calendar with ID: {created_calendar['id']}")
  return created_calendar["id"]

def createEvent(service, name, room, lecturer, start, end, recurrence, color):
  event = {
    "summary": name,
    "location": room,
    "description": lecturer,
    "start": {"dateTime": start, "timeZone": TIMEZONE},
    "end": {"dateTime": end, "timeZone": TIMEZONE}, 
    "recurrence": recurrence, #format: ["RRULE:FREQ=DAILY;COUNT=2"]
    "colorId": color
  }

  return event
    
def insertEvent(service, calendarId, event):
  event = service.events().insert(calendarId=calendarId, body=event).execute()