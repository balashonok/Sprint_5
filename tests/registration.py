import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftests import chrome
from locators import Locators
from data import NEW_EMAIL

class TestRegistration:
    def test_registration_user_registered(self, chrome):
        chrome.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        chrome.find_element(*Locators.REGISTER_LINK).click()
        chrome.find_element(*Locators.NAME_INPUT).send_keys('Ольга')
        chrome.find_element(*Locators.EMAIL_INPUT).send_keys(NEW_EMAIL)
        chrome.find_element(*Locators.PASSWORD_INPUT).send_keys('012345')
        chrome.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(chrome,3).until(expected_conditions.invisibility_of_element(Locators.REGISTER_BUTTON))
        assert chrome.find_element(*Locators.LOGIN_BUTTON)

    @pytest.mark.parametrize('password', ['0', '12', '12345'])
    def test_registration_short_password_error(self, chrome, password):
        chrome.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        chrome.find_element(*Locators.REGISTER_LINK).click()
        chrome.find_element(*Locators.NAME_INPUT).send_keys('Ольга')
        chrome.find_element(*Locators.EMAIL_INPUT).send_keys(NEW_EMAIL)
        chrome.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        chrome.find_element(*Locators.REGISTER_BUTTON).click()
        assert chrome.find_element(*Locators.ERROR_INCORRECT_PASSWORD)