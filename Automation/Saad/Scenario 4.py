from selenium import webdriver
import time

# Initialize the driver
driver = webdriver.Chrome()

# Navigate to the Odoo login page
driver.get("http://localhost:8069/web/login")

# Log in to Odoo
email = driver.find_element_by_name("login")
password = driver.find_element_by_name("password")
email.send_keys("12345678@abc.com")
password.send_keys("12345678")
driver.find_element_by_css_selector("button[type='submit']").click()

# Wait for the page to load
time.sleep(5)

# Navigate to the project page
driver.get("http://localhost:8069/web#menu_id=115&action=376")

# Wait for the page to load
time.sleep(5)

# Click on the "Discussions" tab
driver.find_element_by_xpath("//span[text()='Discussions']").click()

# Wait for the page to load
time.sleep(5)

# Click on the "New Discussion" button
driver.find_element_by_xpath("//button[text()='New Discussion']").click()

# Wait for the page to load
time.sleep(5)

# Enter the discussion title and description
title = driver.find_element_by_name("name")
title.send_keys("Discussion Title")
description = driver.find_element_by_name("description")
description.send_keys("Discussion Description")

# Add team members and stakeholders to the discussion
driver.find_element_by_xpath("//span[text()='Add a member']").click()
driver.find_element_by_xpath("//label[text()='John Smith']").click()
driver.find_element_by_xpath("//span[text()='Add']").click()

# Click on the "Create" button
driver.find_element_by_xpath("//button[text()='Create']").click()

# Wait for the discussion to be created
time.sleep(5)

# Verify that a new discussion thread is created
assert driver.find_element_by_xpath("//h4[text()='Discussion Title']")

# Verify that all members added to the discussion receive a notification
notification_count = driver.find_element_by_xpath("//span[contains(@class, 'o_notification_counter')]")
assert notification_count.text == "1"

# Verify that the discussion is listed on the "Discussions" tab
assert driver.find_element_by_xpath("//div[contains(@class, 'o_mail_discussions')]/div[contains(text(), 'Discussion Title')]")
