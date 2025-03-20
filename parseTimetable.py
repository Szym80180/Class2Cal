# Non-Commercial Open License (NCOL)
# Copyright (c) 2025 Szym80180
# 
# This software is licensed under the Non-Commercial Open License (NCOL).
# You may use, modify, and distribute this code for non-commercial purposes only.
# Redistribution must include attribution to the original author and retain this license.
# For full license details, see the LICENSE file in the project root.

import bs4
import re
from bs4 import BeautifulSoup as bs
from bs4 import SoupStrainer
import bs4

FILENAME = "sis.html"
OUTPUT_FILENAME = "parsed.txt"

def parseHTML():
    try:
        file = open(OUTPUT_FILENAME,"w", encoding = "utf-8") 
    except FileNotFoundError:
        print(f"Nie znaleziono pliku {OUTPUT_FILENAME}")
        input("Wciśnij enter aby zakończyć")
        exit(1)

    only_table = SoupStrainer(id="tb")
    try:
        soup = bs(open(FILENAME, encoding="utf-8"), "html.parser", parse_only=only_table)
    except FileNotFoundError:
        print(f"Nie znaleziono pliku {FILENAME}")
        input("Wciśnij enter aby zakończyć")
        exit(1)


    rows = soup.find_all("tr")

    for row in rows:
        i=0
        for cell in row.find_all("td"):
            file.write("dzien\n")
            if i == 0:
                time = cell.get_text(strip=True)
                file.write(f"{time}\n")
                i += 1
                continue
            if cell.get_text(strip=True)=="":
                file.write("pusty\n")
            else:
                for tag in cell:
                    if tag.name == "br":
                        pass
                    elif tag.get_text(strip=True)=="":
                        pass
                    else:
                        file.write(f"{tag.get_text()}\n")
                        #print(tag.name)

    file.close()
    return