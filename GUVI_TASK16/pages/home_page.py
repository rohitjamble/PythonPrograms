from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    POPULATION=(By.XPATH,"//div[@data-counter-target='display']")

    def get_population(self):
        return self.get_text(self.POPULATION)