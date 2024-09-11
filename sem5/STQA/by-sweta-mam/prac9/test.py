from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("http://localhost:5000")

checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
checked = 0
unchecked = 0

for checkbox in checkboxes:
    if checkbox.is_selected():
        checked += 1
    else:
        unchecked += 1

print(f"Total checkboxes: {len(checkboxes)}")
print(f"Checked: {checked}")
print(f"Unchecked: {unchecked}")

driver.quit()
