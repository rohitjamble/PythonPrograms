from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_courses(driver):
    #Xpath of course
    courses=driver.find_element(By.XPATH,"//p[contains(@class,'⭐️f6lmuc-0 menu-hover') and text()='Courses']")
    #Find parent element
    parent=driver.find_element(By.XPATH,"(//p[text()='Courses'])[1]/..")
    #First Child
    child=driver.find_element(By.XPATH,"(//p[text()='Courses'])[1]/parent::div/child::p[1]")
    #ancestor
    ancestor=driver.find_elements(By.XPATH,"(//p[text()='Courses'])[1]/ancestor::*")
    #Following sibling
    Following=driver.find_elements(By.XPATH,"(//p[text()='Courses'])[1]/following-sibling::*")
    #Preceding-sibling
    Sibling=driver.find_elements(By.XPATH,"(//p[text()='Courses'])[1]/preceding::*")

    assert courses.text == "Courses"
    assert parent.tag_name == "div"
    assert child.tag_name == "p"
    print("courses test passed")



def test_live_cls(driver):
    # Xpath of Live classes
    courses = driver.find_element(By.XPATH, "//p[contains(@class,'⭐️f6lmuc-0 menu-hover') and text()='LIVE Classes']")
    # Find parent element
    parent = driver.find_element(By.XPATH, "(//p[text()='LIVE Classes'])[1]/..")
    # First Child
    child = driver.find_element(By.XPATH, "(//p[text()='LIVE Classes'])[1]/parent::div/child::p[1]")
    # ancestor
    ancestor = driver.find_elements(By.XPATH, "(//p[text()='LIVE Classes'])[1]/ancestor::*")
    # Following sibling
    Following = driver.find_elements(By.XPATH, "(//p[text()='LIVE Classes'])[1]/following-sibling::*")
    # Preceding-sibling
    Sibling = driver.find_elements(By.XPATH, "(//p[text()='LIVE Classes'])[1]/preceding::*")

    assert courses.text == "LIVE Classes"
    assert parent.tag_name == "div"
    assert child.tag_name == "p"
    print("LIVE Classes test passed")

def test_Practice(driver):
    # Xpath of Live classes
    courses = driver.find_element(By.XPATH, "//p[contains(@class,'⭐️f6lmuc-0 menu-hover') and text()='Practice']")
    # Find parent element
    parent = driver.find_element(By.XPATH, "(//p[text()='Practice'])[1]/..")
    # First Child
    child = driver.find_element(By.XPATH, "(//p[text()='Practice'])[1]/parent::div/child::p[1]")
    #Scond sibling
    second_sibling=driver.find_element(By.XPATH,"(//p[text()='Practice'])[1]/../../following-sibling::div[2]")
    # ancestor
    ancestor = driver.find_elements(By.XPATH, "(//p[text()='Practice'])[1]/ancestor::*")
    # Following sibling
    Following = driver.find_elements(By.XPATH, "(//p[text()='Practice'])[1]/following-sibling::*")
    # Preceding-sibling
    Sibling = driver.find_elements(By.XPATH, "(//p[text()='Practice'])[1]/preceding::*")

    assert courses.text == "Practice"
    assert parent.tag_name == "div"
    assert child.tag_name == "p"
    assert second_sibling.get_attribute("q:key")=="km_66"
    print("Practice test passed")

def test_resources(driver):
    # Xpath of Live classes
    courses = driver.find_element(By.XPATH, "//p[contains(@class,'⭐️f6lmuc-0 menu-hover') and text()='Resources']")
    # Find parent element
    parent = driver.find_element(By.XPATH, "(//p[text()='Resources'])[1]/..")
    # First Child
    child = driver.find_element(By.XPATH, "(//p[text()='Resources'])[1]/parent::div/child::p[1]")

    # ancestor
    ancestor = driver.find_elements(By.XPATH, "(//p[text()='Resources'])[1]/ancestor::*")
    # Following sibling
    Following = driver.find_elements(By.XPATH, "(//p[text()='Resources'])[1]/following-sibling::*")
    # Preceding-sibling
    Sibling = driver.find_elements(By.XPATH, "(//p[text()='Resources'])[1]/preceding::*")

    assert courses.text == "Resources"
    assert parent.tag_name == "div"
    assert child.tag_name == "p"
    
    print("Practice test passed")


def test_Products(driver):
    # Xpath of Live classes
    courses = driver.find_element(By.XPATH, "//p[contains(@class,'⭐️f6lmuc-0 menu-hover') and text()='Our Products']")
    # Find parent element
    parent = driver.find_element(By.XPATH, "(//p[text()='Our Products'])[1]/..")
    # First Child
    child = driver.find_element(By.XPATH, "(//p[text()='Our Products'])[1]/parent::div/child::p[1]")
    #secondsibling
    second_sibling = driver.find_element(By.XPATH,"(//p[text()='Our Products'])[1]/../../div[2]")
    # ancestor
    ancestor = driver.find_elements(By.XPATH, "(//p[text()='Our Products'])[1]/ancestor::*")
    # Following sibling
    Following = driver.find_elements(By.XPATH, "(//p[text()='Our Products'])[1]/following-sibling::*")
    # Preceding-sibling
    Sibling = driver.find_elements(By.XPATH, "(//p[text()='Our Products'])[1]/preceding::*")

    assert courses.text == "Our Products"
    assert parent.tag_name == "div"
    assert child.tag_name == "p"

    print("Products test passed")

def test_href_parent(driver):
    parent=driver.find_element(By.XPATH,"//link[@href='https://static.guvi.in']/parent::head")
    assert parent.tag_name == "head"
    print("href parent test passed")
