from selenium import webdriver
from pages.home_page import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.login_page import LoginPage
from utilities.excel_utils import read_test_data,write_result


def test_login(driver):
    test_data= read_test_data()
    for row,test_id,username,password,tester in test_data:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login = LoginPage(driver)
        login.login(username, password)
        try:
            WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))
            result="Test Passed"
        except TimeoutException:
            result="Test Failed"
        write_result(row,result,tester)

        if result == "Test Passed":
            home = HomePage(driver)
            home.logout()