import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



def test_login():
    driver = webdriver.Chrome()
    driver.get("https://www.guvi.in/")
    driver.maximize_window()
    driver.find_element(By.XPATH, "(//button[@id='login-btn'])[1]").click()
    time.sleep(2)
    print(driver.title)

    #validation
    assert driver.title == "HCL GUVI | Login"
    driver.quit()
def test_valid():
    driver = webdriver.Chrome()
    driver.get("https://www.guvi.in/sign-in/")
    driver.maximize_window()
    driver.find_element(By.ID, "email").send_keys("rohitjamble39@gmail.com")
    driver.find_element(By.CSS_SELECTOR,"#password").send_keys("Halloffame@2026")
    driver.find_element(By.XPATH,"//a[@id='login-btn']").click()
    time.sleep(3)
    #validation
    assert driver.current_url == "https://www.guvi.in/courses/"
    driver.quit()
def test_invalid():
    driver = webdriver.Chrome()
    driver.get("https://www.guvi.in/sign-in/")
    driver.maximize_window()
    driver.find_element(By.ID, "email").send_keys("rohitjamble3@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("Halloffame@202")
    driver.find_element(By.XPATH, "//a[@id='login-btn']").click()
    time.sleep(2)
    #validation
    Error= driver.find_element(By.XPATH,"(//div[text()='Incorrect Email or Password'])[1]")
    assert Error.text == "Incorrect Email or Password"
    driver.quit()

def test_box():
    driver = webdriver.Chrome()
    driver.get("https://www.guvi.in/sign-in/")
    driver.maximize_window()
    email=driver.find_element(By.ID, "email")
    password=driver.find_element(By.CSS_SELECTOR,"#password")
    assert email.is_displayed()
    assert password.is_displayed()
    assert email.is_enabled()
    assert password.is_enabled()


def test_submit():
    driver = webdriver.Chrome()
    driver.get("https://www.guvi.in/sign-in/")
    driver.maximize_window()
    driver.find_element(By.ID, "email").send_keys("rohitjamble39@gmail.com")
    driver.find_element(By.CSS_SELECTOR,"#password").send_keys("Halloffame@2026")
    driver.find_element(By.XPATH,"//a[@id='login-btn']").click()
    print(driver.current_url)
    time.sleep(2)
    #validation
    assert driver.current_url == "https://www.guvi.in/courses/"
    driver.quit()


