import calendarHandler as ch
from createEvents import getEvents
import datetime

# date += datetime.timedelta(days=1)


def main():
    start_date=datetime.datetime(2025,3,17)
    current_date = start_date
    def_recurrence = 'RRULE:FREQ=WEEKLY;UNTIL=20250614T170000Z'
    
    
    service = ch.createService()
    if service:
        calendarId = ch.createCalendar(service)
    else:
        print("Failed to create service. Please check your credentials and try again.")

    gr = input("Podaj literę grupy dziekanskiej (A/B): ")
    timetable = getEvents()
    #print(timetable)
    for day in timetable:
        for event in timetable[day]:
            recurrence=def_recurrence
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
            if not 'end' in event:
                end = start.replace(hour=endhour, minute=0, second=0)
            else:
                rec_date = event['end'][3:].replace(".", "")
                rec_year = rec_date[4:]
                rec_month = rec_date[2:4]
                rec_day = rec_date[:2]
                rec_date = rec_year + rec_month + rec_day
                recurrence = 'RRULE:FREQ=WEEKLY;UNTIL=' + rec_date + "T230000Z"
            end = start.replace(hour=endhour, minute=0, second=0)
            
            print(f"{event['type']} {event['name']} {event['room']} {event['lecturer']} {start} {end} {recurrence}")
            #print(recurrence)
            print(f"{event['type']} {event['name']} {event['room']} {event['lecturer']} {start} {end}")
            start = start.isoformat()
            end = end.isoformat()
            pushed_event = ch.createEvent(service, f"{event['type']} {event['name']}", event["room"], f"{event['lecturer']}", start, end, [recurrence], 1)
            ch.insertEvent(service, calendarId, pushed_event)
            #print(pushed_event)

        current_date =current_date+ datetime.timedelta(days=1)
        
if __name__ == "__main__":
    main()