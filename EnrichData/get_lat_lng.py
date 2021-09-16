import requests
import json
import urllib

URL = "https://maps.googleapis.com/maps/api/geocode/json?address="
#res = requests.get(URL+str(page))

with open('allastationer.json') as json_file:
    stations = json.load(json_file)
    for index, station in enumerate(stations):
        print(index)
        try:
            city = station['City']
            adress = station['Adress']
            full_url = URL+urllib.parse.quote(" "+city+" " + adress) + \
                "&key=APIKEY"

            res = requests.get(full_url)
            results = res.json()

            result = results['results'][0]
            station['location'] = result
        except:
            print("failed to fetch for station:", station)


f = open("res.json", "w", encoding="utf-8")
f.write(json.dumps(stations))
f.close()
