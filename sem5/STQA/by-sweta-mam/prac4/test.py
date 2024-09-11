from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Edge()
driver.get("http://127.0.0.1:5500/index.html")

emailbox = driver.find_element(By.ID,"email")
emailbox.send_keys("hello@gmail.com")
time.sleep(4)
passbox = driver.find_element(By.ID,"pass")
passbox.send_keys("1234")
time.sleep(4)
loginbtn = driver.find_element(By.XPATH,"/html/body/form/input[3]")
loginbtn.click()
time.sleep(4)

msg = driver.find_element(By.ID,"para").text

print("Status",msg)

driver.quit()