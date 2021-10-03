import urllib.request
import json

preem_station_url = "https://www.preem.se/api/Stations/AllStations?$filter=FuelTypes/any(x:%20x/Name+eq+%27Bensin%2098%20(E5)%27)&$select=Id,Name,Address,PostalCode,City,PhoneNumber,StationType,StationSort,StationCardImage,OpeningHourWeekdayTime,ClosingHourWeekdayTime,OpeningHourSaturdayTime,ClosingHourSaturdayTime,OpeningHourSundayTime,ClosingHourSundayTime,CoordinateLatitude,CoordinateLongitude,Services/Name,Services/LinkedPage,Services/IconCssClass,FuelTypes/Name,FuelTypes/LinkedPage,FuelTypes/IconCssClass,FuelTypes/TextColor,FuelTypes/BackgroundColor,FuelTypes/BorderColor,FuelTypes/Type,FriendlyUrl,CampaignImage,CampaignUrl,TrailerRentalUrl,IsTrb,IsSaifa,IsSaifaStation,TillhorInternationellaAllianser&$expand=FuelTypes,Services&currentLanguage=sv"
preem_station_url = "https://www.preem.se/api/Stations/AllStations?$filter=FuelTypes/any(x:%20x/Name+eq+%27Bensin%2098%20(E5)%27)&$select=Id,Name,Address,PostalCode,City,PhoneNumber,StationType,StationSort,OpeningHourWeekdayTime,ClosingHourWeekdayTime,OpeningHourSaturdayTime,ClosingHourSaturdayTime,OpeningHourSundayTime,ClosingHourSundayTime,CoordinateLatitude,CoordinateLongitude,FriendlyUrl&$expand=FuelTypes,Services&currentLanguage=sv"
okq8_station_url = "https://www.okq8.se/-/Station/GetGlobalMapStations?appDataSource=9d780912-2801-4457-9376-16c48d02e688"


def pretty_print(data):
    print(json.dumps(data, indent=4, sort_keys=True))


def download(url):
    with urllib.request.urlopen(url) as url:
        stations = json.loads(url.read().decode())
        print("Found {count} stations".format(count=len(stations)))
        return stations


def preem():
    print("Downloading Preem")
    stations = download(preem_station_url)
    # Format to match datamodel- Enrich with latlong?


def okq8():
    print("Downloading OKQ8")
    stations = download(okq8_station_url)
    pretty_print(stations)


# preem()
okq8()
