import calendarHandler as ch
from createEvents import getEvents
import datetime

def getGroup():
    group = input("Podaj grupę dziekańską (A/B): ")
    if group != 'A' and group != 'B':
        print("Podano niepoprawną grupę dziekańską. Spróbuj ponownie.")
        return getGroup()
    return group

def chooseColor():
    print("Wpisz odpowiedni numer")
    print("1. Niebieski")
    print("2. Zielony")
    print("3. Fioletowy")
    print("4. Jasnoczerwony")
    print("5. Żółty")
    print("6. Pomarańczowy")
    print("7. Turkusowy")
    print("8. Szary")
    print("9. Ciemnoniebieski")
    print("10. Ciemnozielony")
    print("11. Ciemnoczerwone")
    color = input("Wybierz kolor: ")
    if color not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
        print("Podano niepoprawny kolor. Spróbuj ponownie.")
        return chooseColor()
    return color
    
def chooseColors():
    colors={
        'P':0,
        'C':0,
        'L':0,
        'W':0
    }
    print("Wybierz kolor dla wydarzenia konkretnego typu:")
    print("1. Wykład")
    colors['[W]'] = chooseColor()
    print("2. Ćwiczenia")
    colors['[C]'] = chooseColor()
    print("3. Laboratoria")
    colors['[L]'] = chooseColor()
    print("4. Projektowe")
    colors['[P]'] = chooseColor()
    return colors

def main():
    start_date=datetime.datetime(2025,3,17)
    current_date = start_date
    def_recurrence = 'RRULE:FREQ=WEEKLY;UNTIL=20250614T170000Z'
    
    gr = getGroup()
    colors=chooseColors()


    service = ch.createService()
    if not service:
        print("Failed to create service. Please check your credentials and try again.")
    calendarId = ch.createCalendar(service)
    
    timetable = getEvents()
    
    for day in timetable:
        for event in timetable[day]:
            recurrence=def_recurrence
            if("group" in event and event["group"] != gr):
                print(f"Skipping event with group {event['group']}")
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

            
            start = start.isoformat()
            end = end.isoformat()
            pushed_event = ch.createEvent(service, f"{event['type']} {event['name']}", event["room"], f"{event['lecturer']}", start, end, [recurrence], colors[event['type']])
            ch.insertEvent(service, calendarId, pushed_event)
            #print(pushed_event)

        current_date =current_date+ datetime.timedelta(days=1)
        
if __name__ == "__main__":
    main()