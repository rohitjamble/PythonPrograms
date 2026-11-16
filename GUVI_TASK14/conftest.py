import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.guvi.in/sign-in/?sourceUri=http%3A%2F%2Fwww.guvi.in%2F')
    yield driver
    driver.quit()
