from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    ICON=(By.XPATH,"(//div[contains(@class,'account-box-toggler' )])[1]")
    LOGOUT=(By.XPATH,"(//p[text()='Sign Out'])[1]")
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_icon(self):
        self.wait.until(EC.element_to_be_clickable(self.ICON)).click()


    def click_sign_out(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT)).click()