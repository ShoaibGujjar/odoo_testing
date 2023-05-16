# odoo_testing

> testing odoo software in unit_testing api_testing
### A top-level directory layout
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







## Contributing


## License
