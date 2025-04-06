import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from urls import URLs

@pytest.fixture()
def chrome():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome()
    driver.get(URLs.MAIN_PAGE)
    yield driver
    driver.quit()
