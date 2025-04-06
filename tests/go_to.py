import pytest

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftests import chrome
from locators import Locators
from data import USER_EMAIL, USER_PASSWORD
from urls import URLs

class TestGoTo:
    def test_go_to_personal_account(self, chrome):
        chrome.get(URLs.LOGIN_PAGE)
        WebDriverWait(chrome, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        chrome.find_element(*Locators.EMAIL_INPUT).send_keys(USER_EMAIL)
        chrome.find_element(*Locators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
        chrome.find_element(*Locators.LOGIN_BUTTON).click()
        chrome.find_element(*Locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(chrome, 3).until(expected_conditions.visibility_of_element_located(Locators.PROFILE))
        assert chrome.find_element(*Locators.PROFILE)

    @pytest.mark.parametrize('button', [Locators.CONSTRUCTOR, Locators.LOGO])
    def test_go_to_constructor_from_personal_account(self, chrome, button):
        chrome.get(URLs.LOGIN_PAGE)
        WebDriverWait(chrome, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        chrome.find_element(*Locators.EMAIL_INPUT).send_keys(USER_EMAIL)
        chrome.find_element(*Locators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
        chrome.find_element(*Locators.LOGIN_BUTTON).click()
        chrome.find_element(*Locators.PERSONAL_ACCOUNT).click()
        chrome.find_element(*button).click()
        assert chrome.find_element(*Locators.MAKE_BURGER_HEADER)
