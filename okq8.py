from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import json
driver = webdriver.Chrome('./chromedriver')
stations = []


driver.get("https://www.okq8.se/pa-stationen/bensinstationer/")

elem = driver.find_element_by_class_name("coi-banner__accept").click()
fuel_list = driver.find_element_by_partial_link_text('Drivmedel')

fuel_list.click()

span = fuel_list.find_element_by_xpath('//span[text()="GoEasy 98 Extra (E5)"]')
driver.execute_script("arguments[0].scrollIntoView();", span)
driver.execute_script("arguments[0].click();", span)

control = driver.find_element_by_xpath('//button[@title="Zooma ut"]')

for i in range(15):
    control.click()

driver.maximize_window()
driver.find_element_by_class_name('link-arrow').click()


table = driver.find_element_by_class_name("globalMap-table-body")

count = 0
while True:
    try:
        next_button = driver.find_element_by_class_name("globalMap-see-more")
        driver.execute_script("arguments[0].scrollIntoView();", next_button)
        next_button.click()
    except:
        break


rows = table.find_elements_by_class_name("globalMap-table-row")

for row in rows:
    address_rows = row.find_elements_by_class_name("globalMap-address")
    source = row.find_element_by_class_name(
        "station-name").get_attribute('href')
    station = {'Station': "OKQ8", 'City': address_rows[0].text,
               'Adress': address_rows[1].text, "Oktan": "Ja", "Source": source}
    stations.append(station)

f = open("okq8.json", "w", encoding="utf-8")


f.write(json.dumps(stations))
f.close()
driver.close()
