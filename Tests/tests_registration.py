from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import ButtonsPageLocators, FieldsPageLocators, OtherPageLocators
from links import UrlLocators

import random

class TestRegistration:
    # Тест 1 (Регистрация пользователя)
    def test_new_user_registration(self, driver):
        driver.get(UrlLocators.URL_MAIN)

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((ButtonsPageLocators.BTN_LOGIN_AND_REGISTRATION)))
        driver.find_element(*ButtonsPageLocators.BTN_LOGIN_AND_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((ButtonsPageLocators.BTN_NEW_USER)))

        driver.find_element(*ButtonsPageLocators.BTN_NEW_USER).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((OtherPageLocators.OTHR_NEW_REGISTRATION_WINDOW)))

        driver.find_element(*FieldsPageLocators.FLD_EMAIL).send_keys(f"test_{random.randint(100, 999)}@test.test")
        driver.find_element(*FieldsPageLocators.FLD_PASSWORD).send_keys("test_password_2025")
        driver.find_element(*FieldsPageLocators.FLD_REPEAT_PASSWORD).send_keys("test_password_2025")
        driver.find_element(*ButtonsPageLocators.BTN_CREATE_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((OtherPageLocators.OTHR_AVATAR)))

        assert len(driver.find_elements(*OtherPageLocators.OTHR_AVATAR)) == 1
        assert driver.find_element(*OtherPageLocators.OTHR_USER_NAME).text == 'User.'

    # Тест 2 (Регистрация пользователя c email не по маске  *******@*******.***)
    def test_new_user_registration_with_unexpected_mask(self, driver):
        driver.get(UrlLocators.URL_MAIN)

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((ButtonsPageLocators.BTN_LOGIN_AND_REGISTRATION)))
        driver.find_element(*ButtonsPageLocators.BTN_LOGIN_AND_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((ButtonsPageLocators.BTN_NEW_USER)))

        driver.find_element(*ButtonsPageLocators.BTN_NEW_USER).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((OtherPageLocators.OTHR_NEW_REGISTRATION_WINDOW)))

        driver.find_element(*FieldsPageLocators.FLD_EMAIL).send_keys(f"test_{random.randint(100, 999)}")
        driver.find_element(*ButtonsPageLocators.BTN_CREATE_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((OtherPageLocators.OTHR_ERROR_MSG)))

        assert driver.find_element(*OtherPageLocators.OTHR_ERROR_MSG).text == "Ошибка"
        assert len(driver.find_elements(*OtherPageLocators.OTHR_FIELD_WITH_ERROR)) == 3


    # Тест 3 (Регистрация уже существующего пользователя)
    def test_existing_user_registration(self, driver):
        driver.get(UrlLocators.URL_MAIN)

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((ButtonsPageLocators.BTN_LOGIN_AND_REGISTRATION)))
        driver.find_element(*ButtonsPageLocators.BTN_LOGIN_AND_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((ButtonsPageLocators.BTN_NEW_USER)))

        driver.find_element(*ButtonsPageLocators.BTN_NEW_USER).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((OtherPageLocators.OTHR_NEW_REGISTRATION_WINDOW)))
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((FieldsPageLocators.FLD_EMAIL)))

        driver.find_element(*FieldsPageLocators.FLD_EMAIL).send_keys("test@test.test")
        driver.find_element(*FieldsPageLocators.FLD_PASSWORD).send_keys("test_password_2025")
        driver.find_element(*FieldsPageLocators.FLD_REPEAT_PASSWORD).send_keys("test_password_2025")
        driver.find_element(*ButtonsPageLocators.BTN_CREATE_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((OtherPageLocators.OTHR_ERROR_MSG)))

        assert driver.find_element(*OtherPageLocators.OTHR_ERROR_MSG).text == "Ошибка"
        assert len(driver.find_elements(*OtherPageLocators.OTHR_FIELD_WITH_ERROR)) == 3