import urllib.request
import json
import http.client
import requests
from datetime import date

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

today = date.today()
today_str = today.strftime("%Y-%m-%d")

preem_station_url = "https://www.preem.se/api/Stations/AllStations?$filter=FuelTypes/any(x:%20x/Name+eq+%27Bensin%2098%20(E5)%27)&$select=Id,Name,Address,PostalCode,City,PhoneNumber,StationType,StationSort,OpeningHourWeekdayTime,ClosingHourWeekdayTime,OpeningHourSaturdayTime,ClosingHourSaturdayTime,OpeningHourSundayTime,ClosingHourSundayTime,CoordinateLatitude,CoordinateLongitude,FriendlyUrl&$expand=FuelTypes,Services&currentLanguage=sv"
okq8_station_url = "https://www.okq8.se/-/Station/GetGlobalMapStations?appDataSource=9d780912-2801-4457-9376-16c48d02e688"
shell_station_url = "https://shellfleetlocator.geoapp.me/api/v1/cf/locations/nearest_to?lat=62.18955&lng=17.6358&with_all[fuels][]=fuelsave_98&autoload=true&travel_mode=driving&avoid_tolls=false&avoid_highways=false&avoid_ferries=false&corridor_radius=5&driving_distances=false&locale=sv_SE&format=json"
qstar_station_url = "https://qstar-backend-prod.herokuapp.com/api/v2/stations/qstar"

circlek_url = "https://www.circlek.se/station-search"
ingo_url = "https://www.ingo.se/station-search"

def pretty_print(data):
    print(json.dumps(data, indent=4, sort_keys=True))
def evaluate(function):
    stations = function()
    print("98 Oktan stations: ", len(stations))
    pretty_print(stations[0])

def download(url):
    try:
        with urllib.request.urlopen(url) as url:
            stations = json.loads(url.read().decode())
            return stations
    except:
        print(Exception, err)
        print("Failed to download from {url})".format(url=url))
        return[]

def preem():
    print("\nDownloading Preem")
    stations = download(preem_station_url)
    result = []
    count = 0
    for station in stations:
        try:
            count += 1
            out = {}
            out["station"] = "Preem"
            out["short_name"] = "Preem " + station.get("Name","")
            out["city"] = station.get("City","")
            out["formatted_address"] = "{address}, {postal_code} {city}, Sverige".format(address=station.get("Address",""),postal_code=station.get("PostalCode",""),city=station.get("City",""))
            out["position"] = {"lat":station.get("CoordinateLatitude",""),"lng": station.get("CoordinateLongitude","")}
            out["id"] = station.get("Id","")
            out["oktan"] = "Ja"
            out["source"] = "https://preem.se"+station.get("FriendlyUrl", "")
            out["distance"] = 0
            out["phone"] = station.get("PhoneNumber","")
            out["updated"] = today_str
            
            result.append(out)
        except Exception as err:
            print(Exception, err)
            print("Failed for station {total}".format(total=count))
    print("{count} of the total {count}".format(count=count))
    return result

def okq8():
    print("\nDownloading OKQ8")

    # Find id for 98 oktan
    data = download(okq8_station_url)
    filters = data.get("filters")
    for filter in filters:
        if filter.get("name") == "Drivmedel":
            fuels = filter.get("values")
            for fuel in fuels:
                if fuel.get("name") == "GoEasy 98 Extra (E5)":
                    fuel_id = fuel.get("id")
                    break
    if fuel_id == None:
        print("Could not find fuel id")
    else:
        # Find stations with 98 oktan
        stations = data["stations"]
        result = []
        total_count = 0
        my_count = 0
        for station in stations:
            try:    
                total_count += 1
                if fuel_id in station.get("offers"):
                    my_count += 1
                    out = {}
                    out["station"] = station.get("net","")
                    out["short_name"] = "{name}, {address}".format(name=station.get("net",""),address=station.get("name",""))
                    out["city"] = station.get("city","")
                    out["formatted_address"] = "{address}, {city}, Sverige".format(address=station.get("address",""),city=station.get("city",""))
                    out["position"] = station.get("position","")
                    out["id"] = station.get("id","")
                    out["oktan"] = "Ja"
                    out["source"] = "https://okq8.se"+station.get("url", "")
                    out["distance"] = 0
                    out["phone"] = station.get("phone","")
                    out["updated"] = today_str
                    result.append(out)
            except Exception as err:
                print(Exception, err)
                print("Failed for station {total}".format(total=total_count))
        print("{my} of the total {total}".format(my=my_count,total=total_count))
        return result

def shell():
    print("\nDownloading Shell")
    stations = download(shell_station_url)
    result = []
    count = 0
    for station in stations:
        try:
            if station.get("country_code") == "SE":
                count += 1
                out = {}
                out["station"] = station.get("brand","")
                out["short_name"] = station.get("name","")
                out["city"] = station.get("city","")
                out["formatted_address"] = "{address}, {postal_code} {city}, Sverige".format(address=station.get("address",""),postal_code=station.get("postcode",""),city=station.get("city",""))
                out["position"] = {"lat":station.get("lat",""),"lng": station.get("lng","")}
                out["id"] = station.get("id","")
                out["oktan"] = "Ja"
                out["source"] = station.get("website_url", "")
                out["distance"] = 0
                out["phone"] = station.get("telephone","")
                out["updated"] = today_str
                result.append(out)
        except Exception as err:
            print(Exception, err)
            print("Failed for station {total}".format(total=count))
    print("{count} of the total {count}".format(count=count))
    return result

def qstar():
    print("\nDownloading Qstar")
    stations = download(qstar_station_url)
    result = []
    count = 0
    for station in stations:
        try:
            if "Bensin 98" in station.get("products"):
                count += 1
                out = {}
                out["station"] = station.get("brand","")
                out["short_name"] = station.get("name","")
                out["city"] = station.get("city","")
                out["formatted_address"] = "{address}, {city}, Sverige".format(address=station.get("address",""),city=station.get("city",""))
                out["position"] = {"lat":station.get("latitude",""),"lng": station.get("longitude","")}
                out["id"] = station.get("id","")
                out["oktan"] = "Ja"
                out["source"] = "https://qstar.se/hitta"
                out["distance"] = 0
                out["phone"] = station.get("phone","")
                out["updated"] = today_str
                result.append(out)
        except Exception as err:
            print(Exception, err)
            print("Failed for station {total}".format(total=count))
    print("{count} of the total {count}".format(count=count))
    return result

def set_empty_dict(content):
    if content is None:
        return dict()
    return content
    
def circlek():
    print("\nDownloading CircleK")
    cookies = {
        'SSESS4b0dcc9eab24632c69fb1df50a2923c3': 'vX2Do2U7R-6WmSJycZJNrxYxOMSksNElEk-gTsKtay9HMHLw',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
    }

    params = (
        ('ajax_form', '1'),
    )

    data = {
    'phrase': '',
    'EU_MILES_98': '1',
    'EU_MILESPLUS_98': '1',
    'form_build_id': 'form-icNimcBJKYBWZ3CRKJqUa6Hl8KQ_maoOcP4OyX3D4pY',
    'form_id': 'sim_search_form',
    '_triggering_element_name': 'op',
    '_triggering_element_value': 'S\xF6k'
    }

    response = requests.post(circlek_url, headers=headers, params=params, cookies=cookies, data=data)
    stations = response.json()[1].get("settings").get("station_results")
    result = []
    count = 0
    for key in stations:
        try:
            station = stations.get(key)
            id = set_empty_dict(station.get("/sites/{{siteId}}{0}".format("")))
            all_addresses = set_empty_dict(station.get("/sites/{{siteId}}/addresses{0}".format("")))
            addresses = set_empty_dict(all_addresses.get("PHYSICAL"))
            contact_details = set_empty_dict(station.get("/sites\{{siteId}}/contact-details{0}".format("")))
            fuels = set_empty_dict(station.get("/sites/{{siteId}}/fuels{0}".format("")))
            location = set_empty_dict(station.get("/sites/{{siteId}}/location{0}".format("")))
            opening_info = set_empty_dict(station.get("/sites/{{siteId}}/opening-info{0}".format("")))

            phone = ""
            phones = contact_details.get("phones")
            if phones is not None:
                for key in phones:
                    phone = phones[key]
                    break
                
            count += 1
            out = {}
          
            out["station"] = id.get("brand","")
            
            out["short_name"] = id.get("name","")
            out["city"] = addresses.get("city","")
            out["formatted_address"] = "{address}, {postal_code} {city}, Sverige".format(address=addresses.get("street",""), postal_code=addresses.get("postalCode",""),city=addresses.get("city",""))
            out["position"] = {"lat":location.get("lat",""),"lng": location.get("lng","")}
            out["id"] = id.get("id","")
            out["oktan"] = "Ja"
            out["source"] = circlek_url
            out["distance"] = 0
            out["phone"] = phone

            out["updated"] = today_str
            result.append(out)
        
        except Exception as err:
            print(Exception, err)
            print("Failed for station {total}".format(total=count))
    print("{count} of the total {count}".format(count=count))
    return result

def ingo():
    print("\nDownloading Ingo")
    cookies = {
        '_gcl_au': '1.1.1144252494.1633095024',
        'at_check': 'true',
        'CookieConsent': '{stamp:\'+QuX5EpHN+UVgh+KHYk/AYxGOMPUZaZyDlsoXAf7/FmrD52RQptRtA==\'%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1633095016266%2Cregion:\'se\'}',
        '_fbp': 'fb.1.1633095026615.1388834457',
        'AMCVS_69F83E625E9932000A495E14%40AdobeOrg': '1',
        'visitor_id908482': '190401803',
        'visitor_id908482-hash': 'be92dd44b762123cb311d793bac22b57707e3ae5983360549df851c5d703fc977c9f7d3a1b5a642ebd7e469d041325476ded92cf',
        'mbox': 'PC#9f7d592d244d48e08d033efa7c178f2a.37_0#1696739836|session#a12e123d620040dc9871bd34cdaf8089#1633496895',
        'AMCV_69F83E625E9932000A495E14%40AdobeOrg': '359503849%7CMCIDTS%7C18907%7CMCMID%7C73538812949575131760693467347632273646%7CMCAAMLH-1634099835%7C6%7CMCAAMB-1634099835%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1633502235s%7CNONE%7CvVersion%7C5.0.1',
        '_gid': 'GA1.2.1648626823.1633495037',
        '_gat_gtag_UA_34402764_30': '1',
        '_gat_gtag_UA_34402764_41': '1',
        '_ga_BYD2EBTLRT': 'GS1.1.1633495043.2.0.1633495043.0',
        '_ga': 'GA1.2.1694181636.1633095025',
        '_timer': '19',
    }

    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Origin': 'https://www.ingo.se',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.ingo.se/station-search',
        'Accept-Language': 'sv-SE,sv;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
    }

    params = (
        ('ajax_form', '1'),
        ('_wrapper_format', 'drupal_ajax'),
    )

    data = {
    'phrase': '',
    'EU_BENZIN_98': '1',
    'form_build_id': 'form-S-7DZObMtp5PBTZxP4NqjBwaNvFCSgCkZcNlh-S5Nj8',
    'form_id': 'sim_search_form',
    '_triggering_element_name': 'op',
    '_triggering_element_value': 'S\xF6k',
    '_drupal_ajax': '1',
    'ajax_page_state[theme]': 'ingo',
    'ajax_page_state[theme_token]': '',
    'ajax_page_state[libraries]': 'circlek/ajax-modal-uikit,circlek/global-css,circlek/global-scripts,circlek/main-menu,ck_cookie_complience/cookie_banner,ck_sim_search/ck_sim_search_map,core/drupal.autocomplete,core/drupal.collapse,core/jquery.form,system/base'
    }

    response = requests.post(ingo_url, headers=headers, params=params, cookies=cookies, data=data)
    stations = response.json()[1].get("settings").get("station_results")
    result = []
    count = 0
    for key in stations:
        try:
            station = stations.get(key)
            id = set_empty_dict(station.get("/sites/{{siteId}}{0}".format("")))
            all_addresses = set_empty_dict(station.get("/sites/{{siteId}}/addresses{0}".format("")))
            addresses = set_empty_dict(all_addresses.get("PHYSICAL"))
            contact_details = set_empty_dict(station.get("/sites\{{siteId}}/contact-details{0}".format("")))
            fuels = set_empty_dict(station.get("/sites/{{siteId}}/fuels{0}".format("")))
            location = set_empty_dict(station.get("/sites/{{siteId}}/location{0}".format("")))
            opening_info = set_empty_dict(station.get("/sites/{{siteId}}/opening-info{0}".format("")))

            phone = ""
            phones = contact_details.get("phones")
            if phones is not None:
                for key in phones:
                    phone = phones[key]
                    break
                
            count += 1
            out = {}
          
            out["station"] = id.get("brand","")
            
            out["short_name"] = id.get("name","")
            out["city"] = addresses.get("city","")
            out["formatted_address"] = "{address}, {postal_code} {city}, Sverige".format(address=addresses.get("street",""), postal_code=addresses.get("postalCode",""),city=addresses.get("city",""))
            out["position"] = {"lat":location.get("lat",""),"lng": location.get("lng","")}
            out["id"] = id.get("id","")
            out["oktan"] = "Ja"
            out["source"] = circlek_url
            out["distance"] = 0
            out["phone"] = phone

            out["updated"] = today_str
            result.append(out)
        
        except Exception as err:
            print(Exception, err)
            print("Failed for station {total}".format(total=count))
    print("{count} of the total {count}".format(count=count))
    return result
def st1():
    print("\nDownloading St1")
    headers = {
        'authority': 'frends.st1.fi',
        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json',
        'x-apikey': 'c286ac79-2684-4c6b-a873-ac1307ebaff6',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://www.st1.se',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.st1.se/',
        'accept-language': 'sv-SE,sv;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
    }

    data = '{"northWestPosition":{"latitude":75.49484595036753,"longitude":-30.69288593749999},"southEastPosition":{"latitude":42.80273595057877,"longitude":60.273910937500006},"searchQuery":"","filters":{"fuels":["sweden/vpower"],"stationTypes":["!sweden/marinestation"],"services":["!sweden/ploq"]},"countryCode":"se"}'

    response = requests.post('https://frends.st1.fi/api/place-locator/v1/find-places/area', headers=headers, data=data)
    data = response.json()
    stations = data.get("stations")
    #pretty_print(data)
    #exit()
    result = []
    count = 0
    for station in stations:
        try:
            count += 1
            out = {}
            out["station"] = station.get("brand","")
            out["short_name"] = station.get("name","")
            out["city"] = station.get("city","")
            out["formatted_address"] = station.get("fullAddress", "")
            location = set_empty_dict(station.get("location"))
            out["position"] = {"lat":location.get("lat",""),"lng": location.get("lon","")}
            out["id"] = station.get("id","")
            out["oktan"] = "Ja"
            out["source"] = "https://www.st1.se/hitta-station?f=%7B%22fuels%22%3A%5B%22sweden%2Fvpower%22%5D%2C%22stationTypes%22%3A%5B%22%21sweden%2Fmarinestation%22%5D%2C%22services%22%3A%5B%22%21sweden%2Fploq%22%5D%7D"
            out["distance"] = 0
            out["phone"] = station.get("telephone","")
            out["updated"] = today_str
            result.append(out)

        except Exception as err:
            print(Exception, err)
            print("Failed for station {total}".format(total=count))
    print("{count} of the total {count}".format(count=count))
    return result


def format_stations(stations):
    for station in stations:
        station["station"] = station.get("station","").title().strip()
        station["short_name"] = station.get("short_name","").title().strip()
        station["city"] = station.get("city","").title().strip()
        station["formatted_address"] = station.get("formatted_address","").title().strip()

        
    return stations

stations = []
stations.extend(qstar())
stations.extend(shell())
stations.extend(preem())
stations.extend(okq8())
stations.extend(circlek())
stations.extend(ingo())
stations.extend(st1())

stations = format_stations(stations)

print("Total stations: ",len(stations))

f = open("stations.json", "w", encoding="utf-8")
f.write(json.dumps(stations))
f.close()

#pretty_print(stations)


