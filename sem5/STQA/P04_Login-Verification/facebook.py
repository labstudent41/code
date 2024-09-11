import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.facebook.com")

email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "pass")
email.send_keys("abcd")
password.send_keys("abcd")

button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")
button.click()

time.sleep(5)
