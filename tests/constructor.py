from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftests import chrome
from locators import Locators
from data import USER_EMAIL, USER_PASSWORD
from urls import URLs

class TestConstructor:
    def test_go_to_buns(self, chrome):
        chrome.get(URLs.LOGIN_PAGE)
        WebDriverWait(chrome, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        chrome.find_element(*Locators.EMAIL_INPUT).send_keys(USER_EMAIL)
        chrome.find_element(*Locators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
        chrome.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(chrome, 3).until(expected_conditions.invisibility_of_element_located(Locators.LOGIN_BUTTON))
        chrome.find_element(*Locators.TUB_FILLINGS).click()
        chrome.find_element(*Locators.TUB_BUNS).click()
        assert chrome.find_element(*Locators.CURRENT_TUB_BUNS).text == 'Булки'

    def test_go_to_sauces(self, chrome):
        chrome.get(URLs.LOGIN_PAGE)
        WebDriverWait(chrome, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        chrome.find_element(*Locators.EMAIL_INPUT).send_keys(USER_EMAIL)
        chrome.find_element(*Locators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
        chrome.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(chrome, 3).until(expected_conditions.invisibility_of_element_located(Locators.LOGIN_BUTTON))
        chrome.find_element(*Locators.TUB_SAUCES).click()
        assert chrome.find_element(*Locators.CURRENT_TUB_SAUCES).text == 'Соусы'

    def test_go_to_fillings(self, chrome):
        chrome.get(URLs.LOGIN_PAGE)
        WebDriverWait(chrome, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        chrome.find_element(*Locators.EMAIL_INPUT).send_keys(USER_EMAIL)
        chrome.find_element(*Locators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
        chrome.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(chrome, 3).until(expected_conditions.invisibility_of_element_located(Locators.LOGIN_BUTTON))
        chrome.find_element(*Locators.TUB_FILLINGS).click()
        assert chrome.find_element(*Locators.CURRENT_TUB_FILLINGS).text == 'Начинки'
