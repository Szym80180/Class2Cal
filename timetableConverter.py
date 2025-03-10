import re
from bs4 import BeautifulSoup as bs
from bs4 import SoupStrainer

FILENAME = "sis.html"

only_table = SoupStrainer(id="tb")
soup = bs(open(FILENAME, encoding="utf-8"), "html.parser", parse_only=only_table)

cells = soup.find_all("tr")
for cell in cells:
    for child in cell.children:
        print(child)





# Tabela idzie wierszami
# 5 list słowników
# 1 lista - jeden dzień
# 1 słownik - jedno wydarzenie



