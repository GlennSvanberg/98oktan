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

url = "https://www.ingo.se/station-search"
driver.get(url)

WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))).click()


driver.find_element_by_class_name("filtering-icon").click()

driver.find_element_by_id("edit-eu-benzin-98").click()
driver.find_element_by_id("new-search").click()
count = 0
running = True
while running:
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "search-result")))

    items = driver.find_elements_by_class_name("search-result")

    for item in items:
        try:
            res = item.find_element_by_class_name(
                "container-station-address").text
            city = res.split(",")[-1].strip()
            address = " ".join(res.split(",")[:-1]).strip()
            count = count + 1
            print(count)
            source = url
            station = {'Station': "Ingo", 'City': city,
                       'Adress': address, "Oktan": "Ja", "Source": source}
            print(station)
            if station not in stations:
                stations.append(station)

        except Exception as e:
            print("failed to get station")
            print(e)
    try:

        print("Clicked next")

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.ID, "next-page")))
        next_button = driver.find_element_by_id("next-page")
        driver.execute_script("arguments[0].scrollIntoView();", next_button)

        next_button.click()

    except Exception as e:
        print(e)
        running = False


f = open("ingo.json", "w", encoding="utf-8")
f.write(json.dumps(stations))
f.close()
driver.close()
