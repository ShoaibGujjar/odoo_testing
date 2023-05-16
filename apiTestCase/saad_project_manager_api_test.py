import unittest
from selenium import webdriver

class ProjectManagerAPITest(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://localhost:8069"  # Odoo URL
        self.email = "12345678@abc.com"  #  email
        self.password = "12345678"  #  password
        
        PATH="C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)  

    def tearDown(self):
        self.driver.quit()

    def test_create_project(self):
        # Login to Odoo
        self.driver.get(self.base_url + "/web/login")
        self.driver.find_element_by_id("login").send_keys(self.email)
        self.driver.find_element_by_id("password").send_keys(self.password)
        self.driver.find_element_by_css_selector(".btn-primary").click()

        # Go to the Project Manager page
        self.driver.get(self.base_url + "/project")

        # Click on the "Create" button to create a new project
        self.driver.find_element_by_css_selector(".o-kanban-button-new").click()

        # Fill in the project details
        self.driver.find_element_by_css_selector("input[name='name']").send_keys("Test Project")
        self.driver.find_element_by_css_selector("textarea[name='description']").send_keys("This is a test project.")
        self.driver.find_element_by_css_selector(".o_form_button_save").click()

        # Assert that the project is created successfully
        success_message = self.driver.find_element_by_css_selector(".o_notification_content").text
        self.assertEqual(success_message, "Project created")

    def test_assign_task(self):
        # Login to Odoo
        self.driver.get(self.base_url + "/web/login")
        self.driver.find_element_by_id("login").send_keys(self.email)
        self.driver.find_element_by_id("password").send_keys(self.password)
        self.driver.find_element_by_css_selector(".btn-primary").click()

        # Go to the Project Manager page
        self.driver.get(self.base_url + "/project")

        # Find the first project in the list
        project_link = self.driver.find_element_by_css_selector(".o_kanban_view .o_kanban_record:nth-child(1) a.o-kanban-box")
        project_link.click()

        # Click on the "Tasks" tab
        self.driver.find_element_by_css_selector(".nav.nav-tabs a[href='#tab-tasks']").click()

        # Click on the "Add a task" button
        self.driver.find_element_by_css_selector(".o_form_button_edit").click()

        # Fill in the task details
        self.driver.find_element_by_css_selector("input[name='name']").send_keys("Test Task")
        self.driver.find_element_by_css_selector("textarea[name='description']").send_keys("This is a test task.")
        self.driver.find_element_by_css_selector("input[name='user_id']").click()
        self.driver.find_element_by_css_selector(".ui-autocomplete li:nth-child(2)").click()
        self.driver.find_element_by_css_selector(".o_form_button_save").click()

        # Assert that the task is assigned successfully
        success_message = self.driver.find_element_by_css_selector(".o_notification_content").text
        self.assertEqual(success_message, "Task created")

if __name__ == "__main__":
    unittest.main()
