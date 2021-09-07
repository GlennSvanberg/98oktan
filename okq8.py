from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome('./chromedriver')

def printStations(rows):
    for row in rows:
        name= row.find_element_by_class_name("station-name")
        print("NAME:",name.text)
        adress_rows = row.find_elements_by_class_name("globalMap-address")
        adress = ""
        for row in adress_rows:
            if adress != "":
                adress= adress + " " + row.text
            else: 
                adress = row.text
        print("Adress:",adress)

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
rows = table.find_elements_by_class_name("globalMap-table-row")
printStations(rows)
while True:
    next_button = driver.find_element_by_class_name("globalMap-see-more")
    driver.execute_script("arguments[0].scrollIntoView();", next_button)
    next_button.click()
    rows = table.find_elements_by_class_name("globalMap-table-row")
    printStations(rows)
