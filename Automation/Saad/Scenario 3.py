from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

# Set up the Chrome driver
driver = webdriver.Chrome()

try:
    # Navigate to the Odoo login page
    driver.get("http://localhost:8069/")
    sign = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
    sign.click()

    # Fill in the login form and submit
    email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login")))
    email.send_keys("12345678@abc.com")
    password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
    password.send_keys("12345678")
    login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Log in']")))
    login.click()

    # Wait for the dashboard page to load
    dashboard = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "o_web_client.o_new_dashboard")))

    # Navigate to the "Tasks" module
    menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Home Menu']")))
    menu.click()
    tasks = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Tasks']")))
    tasks.click()

    # Sort the task list by deadline in ascending order
    sort_by_deadline = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//th[@name='date_deadline']")))
    sort_by_deadline.click()

    # Get the list of tasks and their deadlines
    task_list = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "o_list_view")))
    tasks = task_list.find_elements_by_xpath(".//tbody/tr")
    deadlines = [datetime.strptime(task.find_element_by_xpath(".//td[5]").text, "%Y-%m-%d") for task in tasks]

    # Verify that the tasks are sorted by deadline in ascending order
    assert deadlines == sorted(deadlines)

    # Prioritize the work accordingly
    print("Tasks are sorted by deadline in ascending order. Project manager can prioritize their work accordingly.")
finally:
    # Close the driver
    driver.quit()
