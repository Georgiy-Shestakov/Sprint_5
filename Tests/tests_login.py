from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import ButtonsPageLocators, FieldsPageLocators, OtherPageLocators
from links import UrlLocators
from data import Variables

class TestLogin:
# Тест 4 (Login пользователя)
    def test_login(self, driver):
        driver.get(UrlLocators.URL_MAIN)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((ButtonsPageLocators.BTN_LOGIN_AND_REGISTRATION)))

        driver.find_element(*ButtonsPageLocators.BTN_LOGIN_AND_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((ButtonsPageLocators.BTN_LOGIN)))

        driver.find_element(*FieldsPageLocators.FLD_EMAIL).send_keys(Variables.LOGIN)
        driver.find_element(*FieldsPageLocators.FLD_PASSWORD).send_keys(Variables.PASSWORD)
        driver.find_element(*ButtonsPageLocators.BTN_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((OtherPageLocators.OTHR_AVATAR)))
        
        assert len(driver.find_elements(*OtherPageLocators.OTHR_AVATAR)) == 1
        assert driver.find_element(*OtherPageLocators.OTHR_USER_NAME).text == 'User.'