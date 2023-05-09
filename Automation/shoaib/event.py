import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome() # initialize the Chrome driver
driver.get("http://localhost:8069/") # navigate to your Odoo login page


driver = driver
# find the email input field and enter your email address
time.sleep(2)
sign = driver.find_element("link text","Sign in")
sign.click()
email = driver.find_element("id","login").send_keys("shoaibgujjar948@gmail.com")
password = driver.find_element("id","password").send_keys("shoaib5115")
login = driver.find_element("xpath","//button[text()='Log in']").click()




# navigate to the Events app
driver.get("http://localhost:8069/web#action=344&model=event.event&view_type=kanban&cids=1&menu_id=227")
# events_app_button = driver.find_element("xpath","//a[contains(text(), 'Events')]")
# events_app_button.click()
driver.get("http://localhost:8069/web#cids=1&menu_id=227&action=344&model=event.event&view_type=form")
# click on the Create button to add a new event
# create_event_button = driver.find_element("xpath","//button[contains(text(), 'New')]")
# create_event_button.click()

# fill in the event details
WebDriverWait(driver, 10).until(EC.presence_of_element_located(("name", "name")))
event_name_input = driver.find_element("id","name")
event_name_input.send_keys("Test Event2")
event_start_date_input = driver.find_element("id","date_begin")
event_start_date_input.send_keys("03/04/2023")
event_end_date_input = driver.find_element("id","date_end")
event_end_date_input.send_keys("03/05/2023")
# event_location_input = driver.find_element("id","location")
# event_location_input.send_keys("Online")

# # select the event type from the dropdown menu
# event_type_select = Select(driver.find_element("id","event_type_id"))
# event_type_select.select_by_visible_text("Conference")

# click the Save button to save the new event
save_button = driver.find_element("xpath","//button[contains(text(), 'New')]")
save_button.click()

# wait for the event to be created
time.sleep(5)

# check if the event is displayed in the list of events
event_name_link = driver.find_element("xpath","//a[contains(text(), 'Test Event')]")
assert event_name_link.is_displayed()

# close the driver
driver.quit()