var webdriver = require('selenium-webdriver');
var driver = new webdriver.Builder().build();
driver.sleep(3000);
driver.quit();

