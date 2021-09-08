import requests
import json
import urllib

URL = "https://maps.googleapis.com/maps/api/geocode/json?address="
#res = requests.get(URL+str(page))

with open('stations.json') as json_file:
    data = json.load(json_file)
    for station in data:
        city = station['City']
        adress = station['Adress']
        full_url = URL+urllib.parse.quote(" "+city+" " + adress) + \
            "&key=APIKEY"
        print(full_url)
        res = requests.get(full_url)
        print(res.content)
        break
