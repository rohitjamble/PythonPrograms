from Pages.login_page import LoginPage
from Pages.home_page import HomePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_successfull_login(driver):
    login=LoginPage(driver)

    login.enter_username("rohitjamble39@gmail.com")
    login.enter_password("Halloffame@2026")
    login.click_login_btn()

    home=HomePage(driver)
    home.click_icon()
    home.click_sign_out()


def test_Unsuccessfull_login(driver): #
    login = LoginPage(driver)

    login.enter_username("rohitjamble@gmail.com")
    login.enter_password("Halloffame2026")
    login.click_login_btn()

def test_validate_input_fields(driver): #validation username password and login button
    login = LoginPage(driver)
    #username
    username=login.wait.until(EC.visibility_of_element_located(login.USERNAME))
    assert username.is_displayed()
    assert username.is_enabled()
    # password
    password=login.wait.until(EC.visibility_of_element_located(login.PASSWORD))
    assert password.is_displayed()
    assert password.is_enabled()
    # submit button
    button=login.wait.until(EC.visibility_of_element_located(login.LOGIN_BTN))
    assert button.is_displayed()
    assert button.is_enabled()

def test_logout(driver): #Validating functionality of logout
    login=LoginPage(driver)
    login.enter_username("rohitjamble39@gmail.com")
    login.enter_password("Halloffame@2026")
    login.click_login_btn()

    home = HomePage(driver)
    home.click_icon()
    home.click_sign_out()

    assert "HCL GUVI | Learn to code in your native language" in driver.title