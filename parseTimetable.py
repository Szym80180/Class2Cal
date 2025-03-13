import bs4

import re
from bs4 import BeautifulSoup as bs
from bs4 import SoupStrainer
import bs4

FILENAME = "sis.html"
OUTPUT_FILENAME = "parsed.txt"

file = open(OUTPUT_FILENAME,"w", encoding = "utf-8") 

only_table = SoupStrainer(id="tb")
soup = bs(open(FILENAME, encoding="utf-8"), "html.parser", parse_only=only_table)


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