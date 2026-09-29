import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_possitive_case(driver):
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.NAME, "login-button").click()
    assert "inventory" in driver.current_url
def test_negative_case(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_use")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauc")
    driver.find_element(By.NAME, "login-button").click()
    assert "inventory" not in driver.current_url




