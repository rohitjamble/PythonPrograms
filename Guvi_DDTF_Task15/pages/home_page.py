from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    profile=(By.XPATH,"//span[@class='oxd-userdropdown-tab']")
    logout_btn=(By.XPATH,"//a[normalize-space()='Logout']")

    def logout(self):
        self.click_element(self.profile)
        self.click_element(self.logout_btn)