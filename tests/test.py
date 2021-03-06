# Generated by Selenium IDE
import pytest
import time
import json
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestInterestRate():
  def setup_method(self, method):
    options = Options()
    self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    self.vars = {}

  def teardown_method(self, method):
    self.driver.quit()

  def test_t01_validateDefaults(self):
    # Test name: T01 - Validate default values

    # Open mortgage calculator
    self.driver.get("https://www.zillow.com/mortgage-calculator/")

    # Set window size
    self.driver.set_window_size(1200, 1200)
    logging.debug('Setting window size to 1200x1200')

    # Verify default home price
    value = self.driver.find_element(By.ID, "homePrice").get_attribute("value")
    assert value == "300,000"
    logging.debug('Verifying default home price value')

    # Verify default down payment
    value = self.driver.find_element(By.ID, "form-1_downPayment").get_attribute("value")
    assert value == "60,000"
    logging.debug('Verifying default downpayment value')

    # Verify default down payment percent
    value = self.driver.find_element(By.ID, "form-1_downPaymentPercent").get_attribute("value")
    assert value == "20"
    logging.debug('Verifying default down payment percentage')

    # Verify default loan program
    element = self.driver.find_element(By.ID, "form-1_term")
    locator = "option[@value='{}']".format(element.get_attribute("value"))
    selected_text = element.find_element(By.XPATH, locator).text
    assert selected_text == "30 year fixed"
    logging.debug('Verifying default loan program type')

    # Store default interest rate
    value = self.driver.find_element(By.ID, "rate").get_attribute("value")
    self.vars["defaultRate"] = self.driver.find_element(By.ID, "rate").get_attribute("value")
    print("{}".format(self.vars["defaultRate"]))
    logging.debug('Default interest rate is %f', self.vars["defaultRate"])

    # Store default payment amount
    self.vars["defaultPayment"] = self.driver.find_element(By.CSS_SELECTOR, "g:nth-child(4) > text:nth-child(2)").text
    print("{}".format(self.vars["defaultPayment"]))
    logging.debug('Default payment is %f', self.vars["defaultPayment"])

  def test_t02_validInterestRate(self):
    # Test name: T02 - Using a valid interest rate

    # Open mortgage calculator and validate the default values
    self.test_t01_validateDefaults()

    # Clear interest rate text
    element = self.driver.find_element(By.ID, "rate")
    element.clear()

    # Enter a valid interest rate
    self.driver.find_element(By.ID, "rate").send_keys("3.5")
    logging.debug('Changing interest rate to 3.5%')

    # Click outside of field to commit the value
    self.driver.find_element(By.CSS_SELECTOR, ".rd3-chart").click()

    # Verify new payment amount is different than the default payment
    self.vars["newPayment"] = self.driver.find_element(By.CSS_SELECTOR, "g:nth-child(4) > text:nth-child(2)").text
    assert self.vars["newPayment"] != self.vars["defaultPayment"]
    print("{}".format(self.vars["newPayment"]))
    logging.debug('New payment is %f', self.vars["newPayment"])

  def test_t03_invalidInterestRate(self):
    # Test name: T03 - Using invalid interest rates

    # Open mortgage calculator and validate the default values
    self.test_t01_validateDefaults()

    # Clear interest rate text
    element = self.driver.find_element(By.ID, "rate")
    element.clear()

    # Enter an interest rate less than 0%
    self.driver.find_element(By.ID, "rate").send_keys("-5")

    # Click outside of field to commit the value
    self.driver.find_element(By.CSS_SELECTOR, ".rd3-chart").click()

    # Verify that the below bounds error message is displayed
    elements = self.driver.find_elements(By.XPATH, "//div[@id=\'zmm-calc-payment\']/div/div[2]/div/form/div[4]/p")
    assert len(elements) > 0
    self.vars["lowerBoundMessage"] = self.driver.find_element(By.XPATH, "//div[@id=\'zmm-calc-payment\']/div/div[2]/div/form/div[4]/p").text
    print("{}".format(self.vars["lowerBoundMessage"]))
    logging.debug("{}".format(self.vars["lowerBoundMessage"]))
    assert self.vars["lowerBoundMessage"]== "Rate must be greater than or equal to 0"

    # Clear interest rate text
    element = self.driver.find_element(By.ID, "rate")
    element.clear()

    # Enter an interest rate above 100%
    self.driver.find_element(By.ID, "rate").send_keys("120")

    # Click outside of field to commit the value
    self.driver.find_element(By.CSS_SELECTOR, ".rd3-chart").click()

    # Verify that the above bounds error message is displayed
    elements = self.driver.find_elements(By.XPATH, "//div[@id=\'zmm-calc-payment\']/div/div[2]/div/form/div[4]/p")
    assert len(elements) > 0
    self.vars["upperBoundMessage"] = self.driver.find_element(By.XPATH, "//div[@id=\'zmm-calc-payment\']/div/div[2]/div/form/div[4]/p").text
    print("{}".format(self.vars["upperBoundMessage"]))
    logging.debug("{}".format(self.vars["upperBoundMessage"]))
    assert self.vars["upperBoundMessage"] == "Rate must be less than or equal to 100"

    # Clear interest rate text
    element = self.driver.find_element(By.ID, "rate")
    element.clear()

    # Enter a value that is not a number
    self.driver.find_element(By.ID, "rate").send_keys("abc")

    # Click outside of field to commit the value
    self.driver.find_element(By.CSS_SELECTOR, ".rd3-chart").click()

    # Verify that the "not a number" error message is displayed
    elements = self.driver.find_elements(By.XPATH, "//div[@id=\'zmm-calc-payment\']/div/div[2]/div/form/div[4]/p")
    assert len(elements) > 0
    self.vars["invalidTypeMessage"] = self.driver.find_element(By.XPATH, "//div[@id=\'zmm-calc-payment\']/div/div[2]/div/form/div[4]/p").text
    print("{}".format(self.vars["invalidTypeMessage"]))
    logging.debug("{}".format(self.vars["invalidTypeMessage"]))
    assert self.vars["invalidTypeMessage"] == "'abc' is not a valid number"
