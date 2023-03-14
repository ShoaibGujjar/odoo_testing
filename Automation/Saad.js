module.exports = {
  'Task List: Display Status and Progress': function (browser) {
    browser
      .url('http://localhost:8069')
      .waitForElementVisible('#task-list')
      .click('.task')
      .waitForElementVisible('#task-status')
      .assert.visible('#task-progress');
  },

  'Task List: Adjust Status and Progress on Due Date Change': function (browser) {
    browser
      .url('http://localhost:8069')
      .waitForElementVisible('#task-list')
      .click('.task')
      .waitForElementVisible('#task-due-date')
      .setValue('#task-due-date', '2023-04-01')
      .waitForElementVisible('#task-status')
      .assert.visible('#task-progress');
  },

  'Employee List: Display Personal and Professional Information': function (browser) {
    browser
      .url('http://localhost:8069')
      .waitForElementVisible('#employee-list')
      .click('.employee')
      .waitForElementVisible('#employee-info')
      .assert.visible('#employee-personal-info')
      .assert.visible('#employee-professional-info');
  },

  'Employee List: Prompt User to Enter Required Information on New Employee Record Creation': function (browser) {
    browser
      .url('http://localhost:8069')
      .waitForElementVisible('#employee-list')
      .click('#create-employee')
      .waitForElementVisible('#employee-form')
      .assert.visible('#employee-first-name')
      .assert.visible('#employee-last-name')
      .assert.visible('#employee-email')
      .assert.visible('#employee-phone');
  },

  'Invoices List: Display Details of Selected Invoice': function (browser) {
    browser
      .url('http://localhost:8069')
      .waitForElementVisible('#invoices-list')
      .click('.invoice')
      .waitForElementVisible('#invoice-details')
      .assert.visible('#invoice-due-date')
      .assert.visible('#invoice-amount')
      .assert.visible('#invoice-payment-status');
  },

  'Invoices List: Prompt User to Enter Required Information on New Invoice Creation': function (browser) {
    browser
      .url('http://localhost:8069')
      .waitForElementVisible('#invoices-list')
      .click('#create-invoice')
      .waitForElementVisible('#invoice-form')
      .assert.visible('#invoice-customer-name')
      .assert.visible('#invoice-due-date')
      .assert.visible('#invoice-amount');
  },

  after: function (browser) {
    browser.end();
  }
};
