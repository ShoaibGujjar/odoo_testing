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

# navigate to the Sales app
driver.get("http://localhost:8069/web#action=296&model=sale.order&view_type=list&cids=1&menu_id=178")
# driver.get("http://localhost:8069/web?#menu_id=155&action=144&active_id=channel_inbox")

# click the "Create" button to create a new sales order
create_button = driver.find_element("xpath","//button[text()='new']").click()

# enter the customer's name and select the customer from the dropdown
customer_input = driver.find_element("id","partner_id")
customer_input.send_keys("ACME Corporation")
customer_dropdown = driver.find_element(By.CSS_SELECTOR,".o-autocomplete")
customer_dropdown.find_element("xpath","//li[contains(text(), 'ACME Corporation')]").click()

time.sleep(5)
print("shoaib")
# add a product to the sales order
product_input = driver.find_element("name","product_id")
product_input.send_keys("Product Name")
product_dropdown = driver.find_element("css_selector",".ui-autocomplete")
product_dropdown.find_element("xpath","//li[contains(text(), 'Product Name')]").click()
quantity_input = driver.find_element("name","product_uom_qty")
quantity_input.clear()
quantity_input.send_keys("10")

# save the sales order
save_button = driver.find_element_by_css_selector(".o_form_button_save")
save_button.click()

# verify that the sales order was created
assert "Sales Order" in driver.title
assert "ACME Corporation" in driver.page_source
assert "Product Name" in driver.page_source
assert "10.00" in driver.page_source

driver.close() # close the Chrome driver

