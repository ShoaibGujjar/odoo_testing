from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

# Set up the Chrome driver
driver = webdriver.Edge()

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

# Click on the "Create" button to add a new task
create_button = driver.find_element_by_xpath("//button[contains(text(), 'Create')]")
create_button.click()

# Fill in the task details and assign it to a team member
# ... fill in task form ...

# Click on the "Save" button to save the task
save_button = driver.find_element_by_xpath("//button[contains(text(), 'Save')]")
save_button.click()

# Verify that the task list is updated with the new task
task_name = driver.find_element_by_xpath("//td[@class='o_data_cell o_required_modifier'][contains(text(), 'Task Name')]")
assert task_name.is_displayed()

# Close the driver
driver.quit()
