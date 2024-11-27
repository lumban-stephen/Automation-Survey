import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLScGuzmmOU0BjpZv9AVblmmOVnBCQz5WqMracmAhdOQkZVHqlg/viewform")
driver.maximize_window()

driver.implicitly_wait(20)

locator = "(//span[@class='l4V7wb Fxmcue'])[1]"
driver.find_element(By.XPATH, locator).click()

locator = "(//div[@class='AB7Lab Id5V1'])[4]"
driver.find_element(By.XPATH, locator).click()

locator = "(//div[@class='AB7Lab Id5V1'])[5]"
driver.find_element(By.XPATH, locator).click()


locator = "(//div[@class='AB7Lab Id5V1'])[16]"
driver.find_element(By.XPATH, locator)

time.sleep(10)

