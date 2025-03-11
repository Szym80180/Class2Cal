import re

INPUT_NAME = "parsed.txt"


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

for line in lines:
    if "\n" in line:
        line = line.replace("\n", "")
    if line == "pusty":
        iterator = 0
        input_event = False
        continue
    if re.match(re_hour, line):
        time = line
        continue
    
    if iterator == 0:
        event={}
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
            print(event)
            event={}
            event["time"] = time
            event["room"] = line
            iterator=1
        else:
            iterator=0
            events.append(event)
            print (event)

