from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Launch the browser and navigate to Odoo login page
driver = webdriver.Chrome()
driver.get("http://localhost:8069/web/login")

# Log in as a project manager
email = driver.find_element_by_name("login")
email.send_keys("12345678@abc.com")
password = driver.find_element_by_name("password")
password.send_keys("12345678")
password.send_keys(Keys.RETURN)

# Wait for the dashboard to load and navigate to the project page
time.sleep(5)
project_button = driver.find_element_by_xpath("//a[@href='/web#menu_id=235&action=']")
project_button.click()

# Wait for the project page to load and find an existing discussion thread
time.sleep(5)
discussion_thread = driver.find_element_by_class_name("o_thread_message_content")

# Click on the discussion thread and find the "Attach" button
discussion_thread.click()
attach_button = driver.find_element_by_class_name("o_attach_document")

# Click on the "Attach" button and select a file to upload
attach_button.click()
time.sleep(2)
file_input = driver.find_element_by_xpath("//input[@type='file']")
file_input.send_keys("/path/to/your/file")

# Click on the "Upload" button to attach the file
upload_button = driver.find_element_by_class_name("o_attach_upload")
upload_button.click()
time.sleep(5)

# Verify that the file is attached to the discussion thread
attachment = driver.find_element_by_class_name("o_attachment_preview")
assert attachment.is_displayed()

# Verify that all members added to the discussion receive a notification
notification = driver.find_element_by_class_name("o_mail_notification")
assert notification.is_displayed()

# Close the browser
driver.close()
