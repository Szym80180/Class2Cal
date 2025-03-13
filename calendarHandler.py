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
  """Shows basic usage of the Google Calendar API.
  Prints the start and name of the next 10 events on the user's calendar.
  """
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

def createEvent(service, name, room, lecturer, start, end, recurrence, color):
  event = {
    "summary": name,
    "location": room,
    "description": lecturer,
    "start": {"dateTime": start, "timeZone": TIMEZONE}, #"dateTime": "2022-05-18T09:00:00-07:00", "timeZone": "America/Los_Angeles"
    "end": {"dateTime": end, "timeZone": TIMEZONE}, #{"dateTime": "2022-05-18T17:00:00-07:00", "timeZone": TIMEZONE}
    "recurrence": recurrence, #["RRULE:FREQ=DAILY;COUNT=2"]
    "colorId": color
  }
  #print(f"Event: {event} created")
  return event
    
def insertEvent(service, calendarId, event):
  event = service.events().insert(calendarId=calendarId, body=event).execute()
  print(f"Event inserted: {event.get('htmlLink')}")

if __name__ == "__main__":
  service = createService()
  cid = createCalendar(service)
  event = createEvent(service, "Matematyka", "B1", "Jan Kowalski", "2025-03-10T09:00:00-07:00", "2025-03-10T17:00:00-07:00", ["RRULE:FREQ=DAILY;COUNT=2"], 1)
  insertEvent(service, cid, event)
  x=input("Press x to delete...")
  if(x == "x"):
    service.calendars().delete(calendarId=cid).execute()
  
  
  
  # Call the Calendar API
    #now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
  # events_result = (
    #     service.events()
    #     .list(
    #         calendarId="primary",
    #         timeMin=now,
    #         maxResults=10,
    #         singleEvents=True,
    #         orderBy="startTime",
    #     )
    #     .execute()
    # )
    #events = events_result.get("items", [])
