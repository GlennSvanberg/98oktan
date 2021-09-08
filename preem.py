from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('./chromedriver')
stations = []
driver.maximize_window()

url = "https://www.preem.se/hitta-station#filters=f-1-3"
driver.get(url)
driver.find_element_by_class_name("AcceptCookies-acceptBtn").click()
driver.find_element_by_class_name("StationFinder-showFilterBtn").click()

driver.find_element_by_class_name("StationFinder-showListBtn").click()

res = driver.find_element_by_class_name("List-result")
items = res.find_elements_by_class_name("StationItem")

for item in items:
    city = item.find_element_by_class_name("StationItem-header").text
    address = item.find_element_by_class_name("StationItem-address").text
    print(city,address)
    source = url
    station = {'Station': "Preem", 'City': city,
                'Adress': address, "Oktan": "Ja", "Source": source}

    stations.append(station)
    

f = open("preem.json", "w", encoding="utf-8")
f.write(json.dumps(stations))
f.close()
driver.close()
