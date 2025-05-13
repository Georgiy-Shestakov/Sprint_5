from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import ButtonsPageLocators, FieldsPageLocators, OtherPageLocators, UrlLocators

class Test_logout:
    # Тест 5 (Logout пользователя)
    def test_logout(self, authorised_driver):
        authorised_driver.find_element(*ButtonsPageLocators.BTN_EXIT).click()
        WebDriverWait(authorised_driver, 3).until(expected_conditions.visibility_of_element_located((ButtonsPageLocators.BTN_LOGIN_AND_REGISTRATION)))

        assert len(authorised_driver.find_elements(*OtherPageLocators.OTHR_AVATAR)) == 0
        assert len(authorised_driver.find_elements(*ButtonsPageLocators.BTN_LOGIN_AND_REGISTRATION)) == 1