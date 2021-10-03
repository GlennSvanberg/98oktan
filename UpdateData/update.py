import urllib.request
import json
from datetime import date

today = date.today()
today_str = today.strftime("%Y-%m-%d")

preem_station_url = "https://www.preem.se/api/Stations/AllStations?$filter=FuelTypes/any(x:%20x/Name+eq+%27Bensin%2098%20(E5)%27)&$select=Id,Name,Address,PostalCode,City,PhoneNumber,StationType,StationSort,OpeningHourWeekdayTime,ClosingHourWeekdayTime,OpeningHourSaturdayTime,ClosingHourSaturdayTime,OpeningHourSundayTime,ClosingHourSundayTime,CoordinateLatitude,CoordinateLongitude,FriendlyUrl&$expand=FuelTypes,Services&currentLanguage=sv"
okq8_station_url = "https://www.okq8.se/-/Station/GetGlobalMapStations?appDataSource=9d780912-2801-4457-9376-16c48d02e688"
shell_station_url = "https://shellfleetlocator.geoapp.me/api/v1/cf/locations/nearest_to?lat=62.18955&lng=17.6358&with_all[fuels][]=fuelsave_98&autoload=true&travel_mode=driving&avoid_tolls=false&avoid_highways=false&avoid_ferries=false&corridor_radius=5&driving_distances=false&locale=sv_SE&format=json"
qstar_station_url = "https://qstar-backend-prod.herokuapp.com/api/v2/stations/qstar"

def pretty_print(data):
    print(json.dumps(data, indent=4, sort_keys=True))


def download(url):
    try:
        with urllib.request.urlopen(url) as url:
            stations = json.loads(url.read().decode())
            print("Found {count} stations".format(count=len(stations)))
            return stations
    except:
        print(Exception, err)
        print("Failed to download from {url})".format(url=url))
        return[]

def preem():
    print("Downloading Preem")
    stations = download(preem_station_url)
    result = []
    count = 0
    for station in stations:
        try:
            count += 1
            out = {}
            out["station"] = "Preem"
            out["short_name"] = station.get("Name","")
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
            print("98 Oktan stations: {count} of the total {count}".format(count=count))
    return result

def okq8():
    print("Downloading OKQ8")

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
                    out["short_name"] = station.get("name","")
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
        print("98 Oktan stations: {my} of the total {total}".format(my=my_count,total=total_count))
        return result

def shell():
    print("Downloading Shell")
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
    print("98 Oktan stations: {count} of the total {count}".format(count=count))
    return result

def qstar():
    print("Downloading Qstar")
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
    print("98 Oktan stations: {count} of the total {count}".format(count=count))
    return result
def evaluate(function):
    stations = function()
    print("98 Oktan stations: ", len(stations))
    pretty_print(stations[0])

stations = []
stations.extend(qstar())
stations.extend(shell())
stations.extend(preem())
stations.extend(okq8())

print("Total stations: ",len(stations))