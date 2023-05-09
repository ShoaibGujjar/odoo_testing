import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



driver = webdriver.Firefox() # initialize the Chrome driver
driver.get("http://localhost:8069/") # navigate to your Odoo login page


driver = driver
# find the email input field and enter your email address
time.sleep(2)
sign = driver.find_element("link text","Sign in")
sign.click()
email = driver.find_element("id","login").send_keys("shoaibgujjar948@gmail.com")
password = driver.find_element("id","password").send_keys("shoaib5115")
login = driver.find_element("xpath","//button[text()='Log in']").click()

# assert "Odoo" in driver.title

# navigate to the Sales app
driver.get("http://localhost:8069/web#action=296&model=sale.order&view_type=list&cids=1&menu_id=178")

# click the "Create" button to create a new sales order
time.sleep(5)

search_bar = driver.find_element(By.CSS_SELECTOR,".o_searchview_input")
search_bar.send_keys('azure')
search_bar.send_keys(Keys.RETURN)
time.sleep(5)
# Close the browser
driver.quit()
