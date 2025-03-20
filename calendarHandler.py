# Non-Commercial Open License (NCOL)
# Copyright (c) 2025 Szym80180
# 
# This software is licensed under the Non-Commercial Open License (NCOL).
# You may use, modify, and distribute this code for non-commercial purposes only.
# Redistribution must include attribution to the original author and retain this license.
# For full license details, see the LICENSE file in the project root.


import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.app.created"]
TIMEZONE = "Europe/Warsaw"

def createService():
  
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
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
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

def deleteCalendar(service, calendarId):
  service.calendars().delete(calendarId=calendarId).execute()

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