import calendarHandler as ch
from createEvents import getEvents
import datetime

# date += datetime.timedelta(days=1)


def main():
    start_date=datetime.datetime(2025,3,17)
    current_date = start_date
    recurrence = 'RRULE:FREQ=WEEKLY;COUNT=10'
    
    
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

    gr = input("Podaj literę grupy dziekanskiej (A/B): ")
    timetable = getEvents()
    #print(timetable)
    for day in timetable:
        for event in timetable[day]:
            if("group" in event and event["group"] != gr):
                continue
            hour = (int(event["time"][0:2]))
            endhour = hour + 1
            start = current_date.replace(hour=hour, minute=0, second=0)
            if not 'start' in event:
                start = current_date.replace(hour=hour, minute=0, second=0)
            else:
                startdate = datetime.datetime.strptime(event['start'][3:].replace(".", ""), "%d%m%Y")
                start = startdate.replace(hour=hour, minute=0, second=0)
            end = start.replace(hour=endhour, minute=0, second=0)
            print(f"{event['type']} {event['name']} {event['room']} {event['lecturer']} {start} {end}")
            start = start.isoformat()
            end = end.isoformat()
            pushed_event = ch.createEvent(service, f"{event['type']} {event['name']}", event["room"], f"{event['lecturer']}", start, end, [recurrence], 1)
            ch.insertEvent(service, calendarId, pushed_event)
            #print(pushed_event)

        current_date =current_date+ datetime.timedelta(days=1)
        
if __name__ == "__main__":
    main()