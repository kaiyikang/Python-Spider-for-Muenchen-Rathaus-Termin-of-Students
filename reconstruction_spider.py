import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome()
driver.get("https://www.muenchen.de/rathaus/terminvereinbarung_abh.html?cts=1089339")

jump_iframe = False
while not jump_iframe:
    try:
        driver.switch_to.frame('appointment')
        jump_iframe = True
    except:
        time.sleep(10)


Select(driver.find_element_by_name("CASETYPES[Aufenthaltserlaubnis zum Studium]")).select_by_value('1')

button = driver.find_element(By.XPATH, '//input[@type="submit"]')
button.click()
