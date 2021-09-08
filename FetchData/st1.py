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

url = "https://www.st1.se/hitta-station?f=%7B%22fuels%22%3A%5B%22sweden%2Fvpower%22%5D%7D"
driver.get(url)

WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.CLASS_NAME, "resultset-item")))
total_items = 0

while True:
    items = driver.find_elements_by_class_name("resultset-item")
    if total_items == len(items):
        break
    total_items = len(items)
    print("len", total_items)
    for item in items:
        try:
            title = item.find_element_by_class_name("resultset-item__title")
            driver.execute_script("arguments[0].scrollIntoView();", title)
        except:
            pass


items = driver.find_elements_by_class_name("resultset-item")
for item in items:
    item.find_element_by_class_name("resultset-item__title").click()
    details = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "js-stationlocator-station-details")))

    info = details.find_element_by_class_name("station-details__info")
    name = driver.find_element_by_xpath(
        '//h5[@class="station-details__title"]').text
    address = driver.find_element_by_xpath(
        '//p[@class="station-details__info-item"]').text

    #    a = " ".join(name.split(" ")[1:])

    name = name.replace("Automat", "").strip()
    source = driver.current_url
    city = name.split(" ")[1].strip()

    station = {'Station': "Shell", 'City': city,
               'Adress': address, "Oktan": "Ja", "Source": source}

    print(station)
    stations.append(station)


f = open("st1.json", "w", encoding="utf-8")
f.write(json.dumps(stations))
f.close()
driver.close()
