from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.okq8.se/pa-stationen/bensinstationer/")
print(driver.title)

elem = driver.find_element_by_class_name("coi-banner__accept").click()


fuel_list = driver.find_element_by_partial_link_text('Drivmedel')

fuel_list.click()

span = fuel_list.find_element_by_xpath('//span[text()="GoEasy 98 Extra (E5)"]')
print(span.text)
#actions = ActionChains(driver)
#actions.move_to_element(span).perform()
print("moved")
driver.execute_script("arguments[0].scrollIntoView();", span)
driver.execute_script("arguments[0].click();", span)
map = driver.find_element_by_class_name("globalMap-canvas")
map.send_keys(Keys.SHIFT,Keys.SUBTRACT)
map.send_keys(Keys.SHIFT,Keys.SUBTRACT)
map.send_keys(Keys.SHIFT,Keys.SUBTRACT)
# Markera karta och klicka shift minus för att zooma
