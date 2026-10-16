import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_possitive_dragdrop(driver):
    iframe=driver.find_element(By.XPATH,"//*[@class='demo-frame']")
    driver.switch_to.frame(iframe)
    actions=ActionChains(driver)
    wait=WebDriverWait(driver,10)
    source=wait.until(EC.visibility_of_element_located((By.ID,"draggable")))
    target=wait.until(EC.visibility_of_element_located((By.ID,"droppable")))
    actions.drag_and_drop(source,target).perform()
    time.sleep(2)
    print(target.text)
    assert target.text == "Dropped!"
    driver.switch_to.default_content()

def test_negative_dragdrop(driver):
    iframe=driver.find_element(By.XPATH,"//*[@class='demo-frame']")
    driver.switch_to.frame(iframe)
    actions=ActionChains(driver)
    wait=WebDriverWait(driver,10)
    source=wait.until(EC.visibility_of_element_located((By.ID,"draggable")))
    target=wait.until(EC.visibility_of_element_located((By.ID,"droppable")))
    actions.drag_and_drop_by_offset(source,-200,0).perform()
    time.sleep(2)
    print(target.text)
    assert target.text == "Drop here"
    driver.switch_to.default_content()


