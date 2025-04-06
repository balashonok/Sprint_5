from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftests import chrome
from locators import Locators
from data import USER_EMAIL, USER_PASSWORD
from urls import URLs

class TestLogin:
    def test_login_main_page_login_to_account_button(self, chrome):
        chrome.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        chrome.find_element(*Locators.EMAIL_INPUT).send_keys(USER_EMAIL)
        chrome.find_element(*Locators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
        chrome.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(chrome, 3).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert chrome.find_element(*Locators.ORDER_BUTTON)

    def test_login_personal_account(self, chrome):
        chrome.find_element(*Locators.PERSONAL_ACCOUNT).click()
        chrome.find_element(*Locators.EMAIL_INPUT).send_keys(USER_EMAIL)
        chrome.find_element(*Locators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
        chrome.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(chrome, 3).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert chrome.find_element(*Locators.ORDER_BUTTON)

    def test_login_registration_form_login_link(self, chrome):
        chrome.get(URLs.REGISTER_PAGE)
        chrome.find_element(*Locators.LOGIN_LINK).click()
        WebDriverWait(chrome, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        chrome.find_element(*Locators.EMAIL_INPUT).send_keys(USER_EMAIL)
        chrome.find_element(*Locators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
        chrome.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(chrome, 3).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert chrome.find_element(*Locators.ORDER_BUTTON)

    def test_login_forgot_password_page_login_link(self, chrome):
        chrome.get(URLs.FORGOT_PASSWORD_PAGE)
        chrome.find_element(*Locators.LOGIN_LINK).click()
        chrome.find_element(*Locators.EMAIL_INPUT).send_keys(USER_EMAIL)
        chrome.find_element(*Locators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
        chrome.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(chrome, 3).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert chrome.find_element(*Locators.ORDER_BUTTON)