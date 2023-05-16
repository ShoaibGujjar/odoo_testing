from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()
driver.get("http://localhost:8069/contactus")

elem = driver.find_element("name","name")
elem.send_keys("User")

elem = driver.find_element("name","phone")
elem.send_keys("0300000000")

elem = driver.find_element("name","email_from")
elem.send_keys("user@example.com")

elem = driver.find_element("name","company")
elem.send_keys("Subject")
elem = driver.find_element("name","subject")
elem.send_keys("Subject")

elem = driver.find_element("name","description")
elem.send_keys("description")
time.sleep(2)
submit=driver.find_element("xpath","//a[text()='Submit']").click()
# time.sleep(25)
assert "Thank you for contacting us" in driver.page_source

driver.get("http://localhost:8069/contactus-thank-you")

driver.close()
