from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create an instance of Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the Odoo website
driver.get('http://localhost:8069/')

# Find and click the sign-in link
sign_in_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Sign in')))
sign_in_link.click()

# Fill in the login form and click the Log in button
email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'login')))
email_field.send_keys('12345678@abc.com')
password_field = driver.find_element_by_id('password')
password_field.send_keys('12345678')
log_in_button = driver.find_element_by_xpath('//button[text()="Log in"]')
log_in_button.click()

# Wait for the home page to load and click the "Tasks" module
time.sleep(5)
tasks_module = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[text()="Tasks"]')))
tasks_module.click()

# Sort the tasks by deadline in ascending order
time.sleep(5)
sort_by_deadline_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//th[@name="date_deadline"]/a')))
sort_by_deadline_button.click()

# Verify that the tasks are sorted by deadline in ascending order
time.sleep(5)
tasks_list = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tbody[@class="ui-sortable"]/tr')))
tasks_dates = [task.find_element_by_xpath('.//td[@name="date_deadline"]') for task in tasks_list]
sorted_dates = sorted([date.text for date in tasks_dates])
assert [date.text for date in tasks_dates] == sorted_dates

# Close the browser window
driver.quit()
