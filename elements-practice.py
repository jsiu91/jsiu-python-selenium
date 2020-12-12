#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

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

#Radio Button
driver.get("https://demoqa.com/radio-button")

driver.find_element_by_class_name('custom-control-label').click()

#Web Tables
driver.get("https://demoqa.com/webtables")

driver.find_element_by_id('addNewRecordButton').click()

driver.find_element_by_id('firstName').send_keys('Jonathan')
driver.find_element_by_id('lastName').send_keys('Siu')
driver.find_element_by_id('userEmail').send_keys('jonathansiu@example.com')
driver.find_element_by_id('age').send_keys('29')
driver.find_element_by_id('salary').send_keys('80000')
driver.find_element_by_id('department').send_keys('Engineering')

driver.find_element_by_id('submit').click()

driver.find_element_by_id('searchBox').send_keys('Siu')

#Buttons
driver.get("https://demoqa.com/buttons")

double_click = driver.find_element_by_id('doubleClickBtn')
right_click = driver.find_element_by_id('rightClickBtn')
click_me = driver.find_element_by_xpath("//*[text()='Click Me']")

actions = ActionChains(driver)

actions.double_click(double_click).perform()
actions.context_click(right_click).perform()
actions.click(click_me)

actions.perform()

driver.close()
