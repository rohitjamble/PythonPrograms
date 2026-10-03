import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://www.guvi.in/")
driver.maximize_window()
wait = WebDriverWait(driver,10)
driver.find_element(By.XPATH,"(//button[@id='login-btn'])[1]").click()
time.sleep(2)
print(driver.current_url)
wait.until(EC.visibility_of_element_located((By.ID,"email"))).send_keys("rohitjamble39@gmail.com")
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#password"))).send_keys("Halloffame@2026")
wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@id='login-btn']"))).click()
time.sleep(2)
driver.quit()
# driver.find_element(By.ID,"email").send_keys("rohitjamble39@gmail.com")
# driver.find_element(By.CSS_SELECTOR,"#password").send_keys("Halloffame@2026")
