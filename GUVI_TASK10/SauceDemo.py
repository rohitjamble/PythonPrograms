from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
wait=WebDriverWait(driver,10)

wait.until(EC.visibility_of_element_located((By.ID,"user-name"))).send_keys("standard_user")
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='password']"))).send_keys("secret_sauce")
wait.until(EC.visibility_of_element_located((By.NAME,"login-button"))).click()

print(driver.title)
print(driver.current_url)

content=driver.page_source
with open('Webpage_task_11.txt','w',encoding='utf-8') as file:
    file.write(content)