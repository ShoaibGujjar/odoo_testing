from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

# Set up the Chrome driver
driver = webdriver.Chrome()

# Navigate to the Odoo login page and log in
driver.get("http://localhost:8069/")

# Navigate to the Odoo login page and log in
driver.get("http://localhost:8069/")
# Fill in the login form and submit
email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login")))
email.send_keys("12345678@abc.com")
password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
password.send_keys("12345678")
login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Log in']")))
login.click()

# Wait for the dashboard page to load
dashboard = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "o_web_client.o_new_dashboard")))

# Navigate to the task list page
task_list_button = driver.find_element_by_xpath("//a[@data-menu='250']")
task_list_button.click()

# Select a task and display its status
task = driver.find_element_by_xpath("//td[@class='o_data_cell o_required_modifier']")
task.click()
status = driver.find_element_by_xpath("//span[@name='stage_name']")

# Verify that the status is displayed
assert status.is_displayed()

# Close the driver
driver.quit()
