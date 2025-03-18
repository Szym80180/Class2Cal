import calendarHandler as ch
from createEvents import getEvents
import datetime
import parseTimetable as pt
from gcsa.recurrence import Recurrence
from gcsa.recurrence import SU, MO, TU, WE, TH, FR, SA
from gcsa.recurrence import SECONDLY, MINUTELY, HOURLY, \
                            DAILY, WEEKLY, MONTHLY, YEARLY


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

def getDate():
       
        date = input( "KONIECZNIE WPISZ DATE W FORMACIE DDMMYYYY, inaczej program nie zadziala: ")
        if len(date) != 8 or not date.isdigit():
            print("Podano niepoprawną datę. Spróbuj ponownie.")
            return getDate()
        return date

def createService():
    service = ch.createService()  
    if not service:
        print("Failed to create service. Please check your credentials and try again.")
        exit(1)
    print("Pomyślnie zalogowano do konta Google.")
    return service

def  getStartDate():
    start_date=getDate()
    try:
        start_date = datetime.datetime.strptime(start_date, "%d%m%Y")
    except ValueError:
        print("Podano niepoprawną datę. Spróbuj ponownie.")
        exit(1)
    #if the user didn't input a MONDAY date
    while(start_date.weekday() != 0):
        print("Podana data nie jest poniedziałkiem. Spróbuj ponownie.")
        start_date=getDate()
        try:
            start_date = datetime.datetime.strptime(start_date, "%d%m%Y")
        except ValueError:
            print("Podano niepoprawną datę. Spróbuj ponownie.")
            exit(1)
    return start_date

def getEndDate():
    end_date=getDate()
    try:
        def_until=datetime.datetime.strptime(end_date, "%d%m%Y")+datetime.timedelta(hours=23, minutes=59, seconds=59)
    except ValueError:
        print("Podano niepoprawną datę. Spróbuj ponownie.")
        exit(1)
    return def_until

def handleStartDate(event, current_date, hour):
    if not 'start' in event:
        start = current_date.replace(hour=hour, minute=0, second=0)
    else:
        startdate = datetime.datetime.strptime(event['start'][3:].replace(".", ""), "%d%m%Y")
        start = startdate.replace(hour=hour, minute=0, second=0)
    return start

def handleTwoWeeksStart(event, hour):
    print(f"Data rozpoczęcia zajęć {event['type']} {event['name']} DLA CIEBIE - od tej daty zajęcia beda sie pojawiac co dwa tygodnie:")
    date = getDate()
    startdate = datetime.datetime.strptime(date, "%d%m%Y")
    while startdate.weekday() != event['day']:
        print("Podano niepoprawny dzień tygodnia. Spróbuj ponownie.")
        date = getDate()
        startdate = datetime.datetime.strptime(date, "%d%m%Y")
    start = startdate.replace(hour=hour, minute=0, second=0)
    return start

def checkUntilDate(event, until):
    if 'end' in event:
        rec_date = event['end'][3:].replace(".", "")
        until = datetime.datetime.strptime(rec_date, "%d%m%Y")+datetime.timedelta(hours=23, minutes=59, seconds=59)
    return until


def main():
    pt.parseHTML()
    print("Witaj w programie do automatycznego dodawania zajęć do kalendarza Google!")
    print("Najpierw musisz się zalogować do swojego konta Google.")  
    
    service = createService()

    print("Podaj najbliższy PONIEDZIAŁEK od daty rozpoczęcia zajęć - od tej daty pojawą się zajęcia w kalendarzu")
    start_date=getStartDate() 
    current_date = start_date

    print("Podaj datę zakończenia zajęć - do tej daty pojawiają się zajęcia w kalendarzu")
    def_until=getEndDate()   
    def_interval=1
    
    gr = getGroup()
    colors=chooseColors()
    
    calendarId = ch.createCalendar(service)
    
    timetable = getEvents()
    for day in timetable:
        for event in timetable[day]:
            until = def_until
            interval = def_interval

            #skipping classes for other groups
            if("group" in event and event["group"] != gr):
                continue

            hour = (int(event["time"][0:2]))
            endhour = hour + 1
            start = handleStartDate(event, current_date, hour)            
            until = checkUntilDate(event, until)

            if 'twoweeks' in event:
                interval=2
                start = handleTwoWeeksStart(event, hour)

            recurrence = Recurrence.rule(freq=WEEKLY, until=until, interval=interval, week_start=MO)
            end = start.replace(hour=endhour, minute=0, second=0)
            start = start.isoformat()
            end = end.isoformat()
            pushed_event = ch.createEvent(service, f"{event['type']} {event['name']}", event["room"], f"{event['lecturer']}", start, end, [recurrence], colors[event['type']])
            ch.insertEvent(service, calendarId, pushed_event)
            #print(pushed_event)

        current_date =current_date+ datetime.timedelta(days=1)

    print("Zajęcia zostały dodane do kalendarza.")
    print("Jeżeli zrobiłeś/aś coś źle lub chcesz usnąć kalendarz, wpisz 'delete' i naciśnij ENTER")
    print("Jeżeli chcesz zakończyć program, naciśnij ENTER")
    delete = input()
    if delete == "delete":
        ch.deleteCalendar(service, calendarId)
        print("Kalendarz został usunięty. Jeżeli chcesz ponowić próbę, uruchom program ponownie")
        return
    return
        
if __name__ == "__main__":
    main()