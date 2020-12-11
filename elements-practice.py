#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

chromeOptions = Options()
chromeOptions.headless = True


PATH = "./drivers/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://demoqa.com/text-box")

#Text Box
element = driver.find_element_by_id('userName')
element.send_keys('Jonathan Siu')
element = driver.find_element_by_id('userEmail')
element.send_keys('jonathansiu@gmail.com')
element = driver.find_element_by_id('currentAddress')
element.send_keys('55 Cool st San Francisco CA 94132')
element = driver.find_element_by_id('permanentAddress')
element.send_keys('55 Cool st San Francisco CA 94132')

driver.find_element_by_id('submit').click()



