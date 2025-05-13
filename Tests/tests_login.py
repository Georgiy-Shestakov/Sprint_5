from locators import ButtonsPageLocators, FieldsPageLocators, OtherPageLocators, UrlLocators

class Test_login:
# Тест 4 (Login пользователя)
    def test_login(self, authorised_driver):
        assert len(authorised_driver.find_elements(*OtherPageLocators.OTHR_AVATAR)) == 1
        assert authorised_driver.find_element(*OtherPageLocators.OTHR_USER_NAME).text == 'User.'