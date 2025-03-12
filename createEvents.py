import re
from prettytable import PrettyTable

INPUT_NAME = "parsed.txt"

def next_day(day):
    if day+1 ==5:
        return 0
    return day+1

def insert(day, event):
    if day ==0:
        timetable["monday"].append(event)
    elif day ==1:
        timetable["tuesday"].append(event)
    elif day ==2:
        timetable["wednesday"].append(event)
    elif day ==3:
        timetable["thursday"].append(event)
    elif day ==4:
        timetable["friday"].append(event)

re_hour = r"(\d{2}:\d{2})"
re_grA = r"gr.A"
re_grB = r"gr.B"
re_start = r"od \d{2}.\d{2}.\d{4}"
re_end = r"do \d{2}.\d{2}.\d{4}"
re_twoweeks = r"co 2 tygodnie"

file = open(INPUT_NAME, "r", encoding="utf-8")
lines = file.readlines()

input_event = False
iterator=0
time=0

event = {}
events=[]
timetable={
    "monday": [],
    "tuesday": [],
    "wednesday": [],
    "thursday": [],
    "friday": []
}
day=0
prev_is_time=False
for line in lines:
    
    if "\n" in line:
        line = line.replace("\n", "")
    #print(line)
    if line == "dzien":
        if iterator ==4:
            events.append(event)
            #print(event) 
        if not prev_is_time:
            day = next_day(day)
            #print(f"dzien, przestawiony dzine na {day}")
        iterator = 0
        input_event = False
        continue
    prev_is_time=False
    # if line == "pusty":
    #     day = next_day(day)
    #     print(f"pusty, przestawiony dzine na {day}")
    #     iterator = 0
    #     input_event = False
    #     continue
    
    if re.match(re_hour, line):
        time = line
        day=0
        prev_is_time=True
        continue
    
    if iterator == 0:
        event={}
        event["day"] = day
        event["time"] = time
        event["room"] = line
        iterator += 1
    elif iterator == 1:
        event["type"] = line
        iterator += 1
    elif iterator == 2:
        event["name"] = line
        iterator += 1
    elif iterator == 3:
        event["lecturer"] = line
        iterator += 1
    elif iterator == 4:
        newevent=True
        comments = line
        if re.search(re_grA, comments):
            event["group"] = "A"
            newevent=False
        if re.search(re_grB, comments):
            event["group"] = "B"
            newevent=False
        if re.search(re_start, comments):
            event["start"] = re.search(re_start, comments).group(0)
            newevent=False
        if re.search(re_end, comments):
            event["end"] = re.search(re_end, comments).group(0)
            newevent=False
        if(re.search(re_twoweeks, comments)):
            event["twoweeks"] = True
            newevent=False
        if newevent:
            events.append(event)
            #print (event)
    
#print(events)
for event in events:
    insert(event["day"], event)


