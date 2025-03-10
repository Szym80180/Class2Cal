import calendarHandler as ch

def main():
    service = ch.createService()
    if service:
        calendarId = ch.createCalendar(service)
        event = ch.createEvent(service, "Matematyka", "B1", "Jan Kowalski", "2025-03-10T09:00:00-07:00", "2025-03-10T17:00:00-07:00", ["RRULE:FREQ=DAILY;COUNT=2"], 1)
        ch.insertEvent(service, calendarId, event)
        x = input("Press x to delete...")
        if x == "x":
            service.calendars().delete(calendarId=calendarId).execute()
    else:
        print("Failed to create service. Please check your credentials and try again.")

if __name__ == "__main__":
    main()