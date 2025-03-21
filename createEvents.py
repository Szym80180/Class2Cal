# Non-Commercial Open License (NCOL)
# Copyright (c) 2025 Szym80180
# 
# This software is licensed under the Non-Commercial Open License (NCOL).
# You may use, modify, and distribute this code for non-commercial purposes only.
# Redistribution must include attribution to the original author and retain this license.
# For full license details, see the LICENSE file in the project root.

import re

INPUT_NAME = "parsed.txt"
timetable={
        "monday": [],
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": []
    }
def next_day(day):
    if day+1 ==5:
        return 0
    return day+1

def insert(day, event):
    if day ==0:
        if event not in timetable["monday"]:
            timetable["monday"].append(event)
    elif day ==1:
        if event not in timetable["tuesday"]:
            timetable["tuesday"].append(event)
    elif day ==2:
        if event not in timetable["wednesday"]:
            timetable["wednesday"].append(event)
    elif day ==3:
        if event not in timetable["thursday"]:
            timetable["thursday"].append(event)
    elif day ==4:
        if event not in timetable["friday"]:
            timetable["friday"].append(event)

re_hour = r"^(\d{2}:\d{2})$"
re_grA = r"gr.a"
re_grB = r"gr.b"
re_start = r"od\d{2}.\d{2}.\d{4}"
re_end = r"do\d{2}.\d{2}.\d{4}"
re_twoweeks = r"co2tygodnie"

def getEvents():

    file = open(INPUT_NAME, "r", encoding="utf-8")
    lines = file.readlines()

    input_event = False
    iterator=0
    time=0

    event = {}
    events=[]
    
    day=0
    prev_is_time=False
    for line in lines:

        if "\n" in line:
            line = line.replace("\n", "")
        #print(line)
        
        if line == "dzien":
            if iterator==4:
                events.append(event)
                iterator=0
            if not prev_is_time:
                day = next_day(day)
                #print(f"dzien, przestawiony dzine na {day}")
            iterator = 0
            input_event = False
            continue
        
                #print(event) 
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
            testcomments=line.replace(" ", "").lower().strip()
            if re.search(re_grA, testcomments):
                event["group"] = "a"
                newevent=False
            if re.search(re_grB, testcomments):
                event["group"] = "b"
            if re.search(re_start, testcomments):
                event["start"] = re.search(re_start, testcomments).group(0)
            if re.search(re_end, testcomments):
                event["end"] = re.search(re_end, testcomments).group(0)
            if(re.search(re_twoweeks, testcomments)):
                event["twoweeks"] = True
            events.append(event)
            iterator=0

    #print(events)
    for event in events:
        insert(event["day"], event)
    return timetable


