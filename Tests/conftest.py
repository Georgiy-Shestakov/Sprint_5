import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import UrlLocators, ButtonsPageLocators, FieldsPageLocators, OtherPageLocators

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def authorised_driver(driver):
    driver.get(UrlLocators.URL_MAIN)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((ButtonsPageLocators.BTN_LOGIN_AND_REGISTRATION)))

    driver.find_element(*ButtonsPageLocators.BTN_LOGIN_AND_REGISTRATION).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((ButtonsPageLocators.BTN_LOGIN)))

    driver.find_element(*FieldsPageLocators.FLD_EMAIL).send_keys("test@test.test")
    driver.find_element(*FieldsPageLocators.FLD_PASSWORD).send_keys("123")
    driver.find_element(*ButtonsPageLocators.BTN_LOGIN).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((OtherPageLocators.OTHR_AVATAR)))

    yield driver
