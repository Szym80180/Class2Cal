import re
from bs4 import BeautifulSoup as bs
from bs4 import SoupStrainer
import bs4
FILENAME = "sis.html"

only_table = SoupStrainer(id="tb")
soup = bs(open(FILENAME, encoding="utf-8"), "html.parser", parse_only=only_table)

timetable = {
    "0": [],
    "1": [],
    "2": [],
    "3": [],
    "4": []
}

event = {
    "time": "",
    "name": "",
    "room": "",
    "type": ""
}
time = 0
day=0
i=0
rows = soup.find_all("tr")
for row in rows:
    i=0
    for cell in row.find_all("td"):
        if i == 0:
            time = cell.get_text(strip=True)
            i += 1
        else:
            if cell.get_text(strip=True) == "":
                #print("Empty cell")
                day+=1
                continue
            else:
                for tag in cell.find_all("br"):
                    tag.replace_with(" ")
                for b_tag in cell.find_all("b"):
                    text = b_tag.get_text(strip=True)
                    if re.match(r"\[(C|L|P|W)\]", text):
                        event["type"] = text
                for b_tag in cell.find_all("b"):
                    b_tag.unwrap()         
                for tag in cell.find_all(class_="subject_name"):
                    print(f"Przedmiot: {tag.get_text(strip=True)}")
                    event["name"] = tag.get_text(strip=True)
                    break #wypisuje się tylko jedno
                event["time"] = time
                event["room"] = "TBD"
        print(event)
       



# Tabela idzie wierszami
# 5 list słowników
# 1 lista - jeden dzień
# 1 słownik - jedno wydarzenie



