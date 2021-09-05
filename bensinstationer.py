"""
OKQ8 / tanka 771 / 433 har 98  56 %
https://www.okq8.se/pa-stationen/bensinstationer/
// Karta ej lista

CircleK funklar ej 
https://www.circlek.se/station-search


st1 280 stationer 0 98 oktan 
https://www.st1.se/privat/kundservice/hitta-station

Preem 319 /  157 98 oktan  49 % 
https://www.preem.se/hitta-station
// kartfunktion ej lista

Ingo 291 / 58 st 98 oktan 19 % 
https://www.ingo.se/station-search


Shell 
runt 10 st 98 oktan 

https://www.shell.se/bensinstationer/hitta-shellstationer.html#iframe=Lz9sb2NhbGU9c3ZfU0UjL0A2Mi43OTg0LDYuNjQ5NDcsNXo


Gulf 
67 st / mailat om antalet 98 oktan 
https://gulfsverige.com/hitta-station/


Qstar 
12 st med 98 oktan 
https://www.qstar.se/hitta

"""

import requests
from bs4 import BeautifulSoup

page = 1
max_page = 16
stations = []
for page in range(page, max_page):

    URL = "https://bensinpriser.nu/stationer/98/alla/alla/"
    page = requests.get(URL+str(page))
    soup = BeautifulSoup(page.content)

    table = soup.find(id="price_table")
    rows = table.find_all("tr", class_="table-row")
    for row in rows:
        for br in row.find_all("br"):
            br.replace_with(" ")
        station = row.find_all("td")[0].text
        station = [";".join(s.split(" ", 1)) for s in station]
        station = [";".join(s.split(" ", 2)) for s in station]
        if "TIPS!" not in station:
            stations.append(station)

f = open("stationer.csv", "w", encoding="utf-8")

for station in stations:
    f.write(station + "\n")
f.close()
