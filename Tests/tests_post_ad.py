from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import ButtonsPageLocators, FieldsPageLocators, OtherPageLocators
from links import UrlLocators

import random

class TestPostAd:
    # Тест 6 (Создание объявления неавторизованным пользователем)
    def test_post_ad_unauthorised_user(self, driver):
        driver.get(UrlLocators.URL_MAIN)

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((ButtonsPageLocators.BTN_POST_AN_AD)))
        driver.find_element(*ButtonsPageLocators.BTN_POST_AN_AD).click()

        assert driver.find_element(*OtherPageLocators.OTHR_TO_POST_REGISTER).text == "Чтобы разместить объявление, авторизуйтесь"


    # Тест 7 (Создание объявления авторизованным пользователем)
    def test_post_ad_authorised_user(self, authorised_driver):

        WebDriverWait(authorised_driver, 10).until(expected_conditions.visibility_of_element_located((ButtonsPageLocators.BTN_POST_AN_AD)))
        authorised_driver.find_element(*ButtonsPageLocators.BTN_POST_AN_AD).click()
        name = f"Название {random.randint(100, 999)}"
        authorised_driver.find_element(*FieldsPageLocators.FLD_TITLE).send_keys(name)
        authorised_driver.find_element(*FieldsPageLocators.FLD_DESCRIPTION).send_keys("Какое-то описание")
        authorised_driver.find_element(*FieldsPageLocators.FLD_PRICE).send_keys(random.randint(1, 10000000))

        # WebDriverWait(authorised_driver, 5).until(expected_conditions.visibility_of_element_located((OtherPageLocators.OTHR_CATEGORY_DROPDOWN)))
        authorised_driver.find_element(*OtherPageLocators.OTHR_CATEGORY_DROPDOWN).click()
        authorised_driver.find_element(*OtherPageLocators.OTHR_CATEGORY_DROPDOWN_VARIABLES).click()

        authorised_driver.find_element(*OtherPageLocators.OTHR_CITY_DROPDOWN).click()
        authorised_driver.find_element(*OtherPageLocators.OTHR_CITY_DROPDOWN_VARIABLES).click()

        authorised_driver.find_element(*OtherPageLocators.OTHR_RADIO_CONDITION).click()

        authorised_driver.find_element(*ButtonsPageLocators.BTN_PUBLISH).click()
        WebDriverWait(authorised_driver, 10).until(expected_conditions.url_matches(UrlLocators.URL_MAIN))

        WebDriverWait(authorised_driver, 10).until(expected_conditions.element_to_be_clickable(ButtonsPageLocators.BTN_AVATAR))
        old_button = authorised_driver.find_element(*ButtonsPageLocators.BTN_AVATAR)

        WebDriverWait(authorised_driver, 10).until(expected_conditions.staleness_of(old_button))

        WebDriverWait(authorised_driver, 10).until(expected_conditions.element_to_be_clickable(ButtonsPageLocators.BTN_AVATAR)).click()

        WebDriverWait(authorised_driver, 10).until(expected_conditions.url_matches(UrlLocators.URL_PROFILE))

        WebDriverWait(authorised_driver, 10).until(expected_conditions.visibility_of_element_located((ButtonsPageLocators.BTN_NEXT_PAGE)))

        next_page_button = authorised_driver.find_element(*ButtonsPageLocators.BTN_NEXT_PAGE)
        while next_page_button.is_enabled():
            next_page_button.click()

        old_button = authorised_driver.find_element(*OtherPageLocators.OTHR_LAST_AD)
        WebDriverWait(authorised_driver, 10).until(expected_conditions.staleness_of(old_button))
        element = WebDriverWait(authorised_driver, 3).until(expected_conditions.element_to_be_clickable(OtherPageLocators.OTHR_LAST_AD))

        assert element.text == name