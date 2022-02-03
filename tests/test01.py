# Generated by Selenium IDE
import unittest
import pytest
import time
import json
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

class TestT01Entervalidinterestrate():
  def setup_method(self, method):
    options = Options()
    self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    self.vars = {}

  def teardown_method(self, method):
    self.driver.quit()

  def test_t01Entervalidinterestrate(self):
    # Test name: T01 - Enter valid interest rate
    # Step # | name | target | value

    # 1 | open | https://www.zillow.com/mortgage-calculator/ |
    # Open mortgage calculator
    self.driver.get("https://www.zillow.com/mortgage-calculator/")

    # 2 | setWindowSize | 1167x1053 |
    self.driver.set_window_size(1167, 1053)

    # 3 | verifyValue | id=homePrice | 300,000
    # Verify default home price
    value = self.driver.find_element(By.ID, "homePrice").get_attribute("value")
    assert value == "300,000"

    # 4 | verifyValue | id=form-1_downPayment | 60,000
    # Verify default down payment
    value = self.driver.find_element(By.ID, "form-1_downPayment").get_attribute("value")
    assert value == "60,000"

    # 5 | verifyValue | id=form-1_downPaymentPercent | 20
    # Verify default down payment percent
    value = self.driver.find_element(By.ID, "form-1_downPaymentPercent").get_attribute("value")
    assert value == "20"

    # 6 | verifySelectedLabel | id=form-1_term | 30 year fixed
    # Verify default loan program
    element = self.driver.find_element(By.ID, "form-1_term")
    locator = "option[@value='{}']".format(element.get_attribute("value"))
    selected_text = element.find_element(By.XPATH, locator).text
    assert selected_text == "30 year fixed"

    # 7 | verifyValue | id=rate | 3.668
    # Verify default interest rate
    value = self.driver.find_element(By.ID, "rate").get_attribute("value")
    assert value == "3.647"

    # 8 | verifyText | css=g:nth-child(4) > text:nth-child(2) | $1,415
    # Verify default payment
    assert self.driver.find_element(By.CSS_SELECTOR, "g:nth-child(4) > text:nth-child(2)").text == "$1,413"

    # 9 | doubleClick | id=rate |
    # Select interest rate text
    element = self.driver.find_element(By.ID, "rate")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()

    # 10 | type | id=rate | 3.5
    # Enter valid interest rate
    self.driver.find_element(By.ID, "rate").send_keys("3.5")

    # 11 | click | css=.rd3-chart |
    # Click outside of field to commit the value
    self.driver.find_element(By.CSS_SELECTOR, ".rd3-chart").click()

    # 12 | waitForText | css=g:nth-child(4) > text:nth-child(2) | $1,393
    # Verify new payment
    WebDriverWait(self.driver, 30).until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, "g:nth-child(4) > text:nth-child(2)"), "$1,393"))
