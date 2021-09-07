
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

url = "https://www.circlek.se/station-search"
driver.get(url)


cookie_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")))
cookie_button.click()

driver.find_element_by_class_name("filtering-icon ").click()
driver.find_element_by_id("edit-eu-miles-98").click()
driver.find_element_by_id("edit-eu-milesplus-98").click()
driver.find_element_by_id("new-search").click()


while True:
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "search-result")))

    results = driver.find_elements_by_class_name("search-result")

    for res in results:
        address = res.find_element_by_class_name(
            "container-station-address").text
        address_rows = address.split(",")

        source = url
        station = {'Station': "Cirkle K", 'City': address_rows[1].strip(),
                   'Adress': address_rows[0].strip(), "Oktan": "Ja", "Source": source}

        stations.append(station)

    try:
        driver.find_element_by_id("next-page").click()
    except:
        break


f = open("circle_k.json", "w", encoding="utf-8")
f.write(json.dumps(stations))
f.close()
driver.close()
