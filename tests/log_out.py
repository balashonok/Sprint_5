from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftests import chrome
from locators import Locators
from data import USER_EMAIL, USER_PASSWORD
from urls import URLs

class TestLogOut:
    def test_log_out(self, chrome):
        chrome.get(URLs.LOGIN_PAGE)
        WebDriverWait(chrome, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        chrome.find_element(*Locators.EMAIL_INPUT).send_keys(USER_EMAIL)
        chrome.find_element(*Locators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
        chrome.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(chrome, 3).until(expected_conditions.invisibility_of_element_located(Locators.LOGIN_BUTTON))
        chrome.get(URLs.PERSONAL_ACCOUNT)
        WebDriverWait(chrome, 3).until(expected_conditions.element_to_be_clickable(Locators.LOG_OUT))
        chrome.find_element(*Locators.LOG_OUT).click()
        WebDriverWait(chrome, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        assert chrome.find_element(*Locators.LOGIN_BUTTON).is_displayed()
