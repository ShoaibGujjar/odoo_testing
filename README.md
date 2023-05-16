# README.md

## Odoo Testing

This repository contains various types of testing done on Odoo. The aim of these tests is to ensure that the Odoo modules are functioning as expected and to identify any issues or bugs that need to be addressed. The tests include:

- API testing using Python Requests library
- Automated user story testing using Selenium WebDriver and Gherkin scenarios
- User stories for testing different parts of Odoo
- Gherkin scenarios of user stories
- Static Application Security Testing (SAST) using Bandit
- Performance testing using Locust
- Code quality testing using pylint, flake8, and bandit

## A top-level directory layout

```ruby
odoo_testing
├── apiTestCase
│   ├── test_create_sales_order.py        # test case that create new sales in sales app using api
│   ├── test_delete_sales_order.py        # test case that delete sales in sales app passing sale id
│   └── test_update_sales_order.py        # test case that update sales passing sale_id in params 
├── automation 
│   ├── contactUs.py                      # fill form and submit content form
│   ├── searchSales.py                    # search all sales that have "azure" in there name
│   └── event.py                          # create event that going to be happened
├── gherkinScenarios
│   ├── sales                             # all possible scenario in sales app
│   ├── login                             # all possible scenario in login app
│   └── search                            # search sales in sale app
├── unitTest 
│   ├── TestCreateSalesOrder.py           # Table of contents
│   ├── TestDeleteSalesOrder.py           # Frequently asked questions
│   └── TestUpdateSalesOrder.py           # Miscellaneous information
├── userStory
│   ├── story                             # all user story
│   └── ...
├── .gitignore
├── configuration.py                      # add all configurations credentials URl pthh 
├── README.md                             # odoo_testin detail
└── env                                   # environments that run project and install all dependencies in that environments
```


## Getting Started

Before running the tests, the following steps need to be taken:

- Install the required Python libraries by running `pip install -r requirements.txt`
- Set up the Odoo server and install the necessary modules
- Configure the baseURL, userName, password, etc. in the Configuration.py file

## Running the Tests

### API Testing

To run the API tests, navigate to the `apiTestCase` directory and run the `saad_project_manager_api_test.py`, `shoaib_api_test_case.py` file.

### Automated User Story Testing

To run the automated user story tests, navigate to the `Automation` directory and run the available files in directories.

### User Stories and Gherkin Scenarios

The user stories and Gherkin scenarios can be found in the `userstory` and `gherkin scenarios` directories, respectively.

### SAST

To run the SAST, navigate to the `SAST` directory and run the `saad_sast.py` file.

### Performance Testing

To run the performance tests, navigate to the `Performance Testing` directory and run the `saad_performance_test.py` file.

### Code Quality

To run the code quality tests, navigate to the `Code quality` directory and run the `saad_quality_analysis.py` file.

## Contributing

Contributions to this repository are welcome. If you find any issues or have suggestions for improvement, please create a pull request.

## License
None
