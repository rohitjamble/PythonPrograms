#We keep common methods in Base page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    def get_text(self, locator):
        element = self.get_element(locator)
        return element.text