import calendarHandler as ch
from createEvents import getEvents
import datetime

# date += datetime.timedelta(days=1)


def main():
    start_date=datetime.datetime(2025,3,17)
    current_date = start_date
    recurrence = 'RRULE:FREQ=WEEKLY;UNTIL=20250430T1300000Z'
    service = ch.createService()
    if service:
        calendarId = ch.createCalendar(service)
        #event = ch.createEvent(service, "Matematyka", "B1", "Jan Kowalski", "2025-03-10T09:00:00-07:00", "2025-03-10T17:00:00-07:00", ["RRULE:FREQ=DAILY;COUNT=2"], 1)
        #ch.insertEvent(service, calendarId, event)
        # x = input("Press x to delete...")
        # if x == "x":
        #     service.calendars().delete(calendarId=calendarId).execute()
    else:
        print("Failed to create service. Please check your credentials and try again.")

    timetable = getEvents()
    print(timetable)
    for day in timetable:
        for event in timetable[day]:
            hour = (int(event["time"][0:2]))
            endhour = hour + 1
            start = current_date.replace(hour=hour, minute=0, second=0)
            end = current_date.replace(hour=endhour, minute=0, second=0)
            start = start.isoformat()
            end = end.isoformat()
            pushed_event = ch.createEvent(service, f"{event['type']} {event['name']}", event["room"], f"{event['lecturer']}", start, end, [recurrence], 1)
            ch.insertEvent(service, calendarId, pushed_event)
            print(pushed_event)

        current_date =current_date+ datetime.timedelta(days=1)
        
if __name__ == "__main__":
    main()