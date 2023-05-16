import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from configuration import baseUrl,userName,password,saleAppUrl

driver = webdriver.Firefox() # initialize the Chrome driver
driver.get(baseUrl) # navigate to your Odoo login page

driver = driver
time.sleep(2)
# find the 'Sign in' button name and click
sign = driver.find_element("link text","Sign in")
sign.click()
email = driver.find_element("id","login").send_keys(userName)
password = driver.find_element("id","password").send_keys(password)
login = driver.find_element("xpath","//button[text()='Log in']").click()

# navigate to the Sales app
driver.get(saleAppUrl)
time.sleep(5)

# searching 'searchview_input' selector by css selector
search_bar = driver.find_element(By.CSS_SELECTOR,".o_searchview_input")
search_bar.send_keys('azure')
search_bar.send_keys(Keys.RETURN)
time.sleep(5)

# Close the browser
driver.quit()
