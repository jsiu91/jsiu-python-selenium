#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

chromeOptions = Options()
chromeOptions.headless = True


PATH = "./drivers/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("http://thedemosite.co.uk/addauser.php")

#Creating a user
username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')

username.send_keys('abcd')
password.send_keys('abc123')

save_button = driver.find_element_by_name('FormsButton2')
save_button.click()

#Loging in
driver.get("http://thedemosite.co.uk/login.php")

username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')

username.send_keys('abcd')
password.send_keys('abc123')

save_button = driver.find_element_by_name('FormsButton2')
save_button.click()
