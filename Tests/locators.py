from selenium.webdriver.common.by import By
import random
from data import Variables

class ButtonsPageLocators:
    BTN_LOGIN_AND_REGISTRATION = (By.XPATH, ".//div[@class='header_flexRow__Xdqv1']/button[@type='button' and @class='buttonSecondary inButtonText undefined inButtonText']")
    BTN_NEW_USER = (By.XPATH, ".//div[@class='popUp_buttonRow__+W8JD']/button[@type='button' and @class='buttonSecondary inButtonText undefined inButtonText']")
    BTN_CREATE_ACCOUNT = (By.XPATH, ".//*[@class='popUp_buttonRow__+W8JD']/button[@class='buttonPrimary inButtonText undefined inButtonText']")
    BTN_POST_AN_AD = (By.XPATH, ".//div[@class='header_flexRow__Xdqv1']/button[text()='Разместить объявление']")
    BTN_LOGIN = (By.XPATH, ".//div[@class='popUp_buttonRow__+W8JD']/button[@type='submit' and @class='buttonPrimary inButtonText undefined inButtonText']")
    BTN_EXIT = (By.XPATH, ".//div/*[@class='spanGlobal btnSmall' and text()='Выйти']")
    BTN_PUBLISH = (By.XPATH, ".//button[@class='buttonPrimary inButtonText undefined inButtonText' and text()='Опубликовать']")
    BTN_AVATAR = (By.XPATH, "//button[@class='circleSmall']")
    BTN_NEXT_PAGE = (By.XPATH, ".//button[@class='arrowButton arrowButton--right undefined']")

class FieldsPageLocators:
    FLD_EMAIL = (By.XPATH, ".//*[@class='input_inputStandart__JweLZ spanGlobal' and @placeholder='Введите Email']")
    FLD_PASSWORD = (By.XPATH, ".//*[@class='input_inputStandart__JweLZ spanGlobal' and @placeholder='Пароль']")
    FLD_REPEAT_PASSWORD = (By.XPATH, ".//*[@class='input_inputStandart__JweLZ spanGlobal' and @placeholder='Повторите пароль']")
    FLD_TITLE = (By.XPATH, ".//div[@class='input_inputDefault__UmPK0']/input[@placeholder='Название']")
    FLD_DESCRIPTION = (By.XPATH, ".//div[@class='textarea_inputDefault__KvlMg']/textarea[@placeholder='Описание товара']")
    FLD_PRICE = (By.XPATH, ".//div[@class='input_inputDefault__UmPK0']/input[@placeholder='Стоимость']")

class OtherPageLocators:
    OTHR_NEW_REGISTRATION_WINDOW = (By.CLASS_NAME, "popUp_shell__LuyqR")
    OTHR_FIELD_WITH_ERROR = (By.CLASS_NAME, "input_inputError__fLUP9")
    OTHR_CATEGORY_DROPDOWN = (By.XPATH, "//div[@class='dropDownMenu_input__itKtw']/button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP']")
    OTHR_CATEGORY_DROPDOWN_VARIABLES = (By.XPATH, f".//span[text()='{random.choice(Variables.OTHR_CATEGORIES_LIST)}']")
    OTHR_CITY_DROPDOWN = (By.XPATH, ".//div[@class='dropDownMenu_input__itKtw' and @style='margin: 0px; max-width: 760px; width: 100%;']/button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP']")
    OTHR_CITY_DROPDOWN_VARIABLES = (By.XPATH, f".//span[text()='{random.choice(Variables.OTHR_CITIES_LIST)}']")
    OTHR_RADIO_CONDITION = (By.XPATH, ".//div[@class='radioUnput_inputRegular__FbVbr']")
    OTHR_ERROR_MSG = (By.XPATH, ".//span[@class='input_span__yWPqB' and text()='Ошибка']")
    OTHR_AVATAR = (By.XPATH, ".//*[@class='svgSmall']")
    OTHR_MY_PROFILE = (By.XPATH, ".//div/*[text()='Мой профиль']")
    OTHR_USER_NAME = (By.XPATH, ".//*[@class='profileText name']")
    OTHR_TO_POST_REGISTER = (By.XPATH, ".//div[@class='popUp_titleRow__M7tGg']/*[text()='Чтобы разместить объявление, авторизуйтесь']")
    OTHR_LAST_AD = (By.XPATH, ".//div[@class='card'][last()]/div/div[last()-1]/h2")
