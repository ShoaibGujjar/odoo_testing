import unittest
from odoo import models

class TestCreateProject(unittest.TestCase):
    def setUp(self):
        self.env = models.Environment()
    
    def test_create_project(self):
        """Test that the create_project function creates a new project correctly."""
        expected_result = {
            "name": "Test Project",
            "description": "This is a test project."
        }
        
        # Create a new project in Odoo.
        project = self.env["project.project"].create({
            "name": "Test Project",
            "description": "This is a test project."
        })
        
        # Assert that the project was created successfully.
        self.assertEqual(project.name, expected_result["name"])
        self.assertEqual(project.description, expected_result["description"])

class TestAssignTask(unittest.TestCase):
    def setUp(self):
        self.env = models.Environment()
    
    def test_assign_task(self):
        """Test that the assign_task function assigns a task correctly."""
        # Create a new project in Odoo.
        project = self.env["project.project"].create({
            "name": "Test Project",
            "description": "This is a test project."
        })
        
        # Create a new task and assign it to the project.
        task = self.env["project.task"].create({
            "name": "Test Task",
            "project_id": project.id
        })
        
        # Assert that the task was assigned to the project successfully.
        self.assertEqual(task.project_id, project.id)

if __name__ == "__main__":
    unittest.main()

###################################################################################################



# from selenium import webdriver
# import unittest

# class TestProjectManager(unittest.TestCase):
#     def setUp(self):
#         # Set up the Selenium WebDriver
#         self.driver = webdriver.Chrome('path_to_chromedriver')
#         self.driver.implicitly_wait(10)  # Implicitly wait for elements to be found
        
#         # Login to Odoo
#         self.driver.get('http://localhost:8069')
#         self.driver.find_element_by_id('login').send_keys('12345678@abc.com')
#         self.driver.find_element_by_id('password').send_keys('12345678')
#         self.driver.find_element_by_css_selector('.btn.btn-primary').click()
    
#     def tearDown(self):
#         # Close the browser
#         self.driver.quit()
    
#     def test_create_project(self):
#         """Test that the create project functionality works correctly."""
#         # Navigate to the Projects page
#         self.driver.find_element_by_css_selector('.o_menu_systray .o_app[data-menu-xmlid="project.menu_main_pm"]').click()
        
#         # Click on the Create button to open the project creation form
#         self.driver.find_element_by_css_selector('.o-kanban-button-new.o-kanban-button-new-default').click()
        
#         # Fill in the project details
#         self.driver.find_element_by_css_selector('.o_form_input[name="name"]').send_keys('Test Project')
#         self.driver.find_element_by_css_selector('.o_form_input[name="description"]').send_keys('This is a test project.')
        
#         # Save the project
#         self.driver.find_element_by_css_selector('.o_form_button_save').click()
        
#         # Verify that the project is created successfully
#         project_name = self.driver.find_element_by_css_selector('.o_form_field[name="name"] span').text
#         project_description = self.driver.find_element_by_css_selector('.o_form_field[name="description"] span').text
        
#         self.assertEqual(project_name, 'Test Project')
#         self.assertEqual(project_description, 'This is a test project.')
    
#     def test_assign_task(self):
#         """Test that the assign task functionality works correctly."""
#         # Navigate to the Projects page
#         self.driver.find_element_by_css_selector('.o_menu_systray .o_app[data-menu-xmlid="project.menu_main_pm"]').click()
        
#         # Open an existing project
#         self.driver.find_element_by_css_selector('.o-kanban-button:first-child .o_project_kanban_content').click()
        
#         # Click on the Create button to open the task creation form
#         self.driver.find_element_by_css_selector('.o-kanban-button-new.o-kanban-button-new-default').click()
        
#         # Fill in the task details
#         self.driver.find_element_by_css_selector('.o_form_input[name="name"]').send_keys('Test Task')
        
#         # Save the task
#         self.driver.find_element_by_css_selector('.o_form_button_save').click()
        
#         # Verify that the task is assigned to the project
#         task_name = self.driver.find_element_by_css_selector('.o_form_field[name="name"] span').text
#         project_name = self.driver.find_element_by_css_selector('.o_form_field[name="project_id"] span').text
        
#         self.assertEqual(task_name, 'Test Task')
#         self.assertEqual(project_name, 'Test Project')
        

# if __name__ == '__main__':
#     unittest.main()

