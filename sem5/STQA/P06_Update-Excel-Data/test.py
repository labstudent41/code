from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://127.0.0.1:5000")
table = driver.find_element(By.ID, 'student-table')
rows = table.find_elements(By.TAG_NAME, 'tr')

toppers = {'English': ['', 0],
           'Hindi': ['', 0],
           'Marathi': ['', 0]}
students_above_60 = []

for row in rows[1:]:
    cells = row.find_elements(By.TAG_NAME, 'td')
    english = int(cells[3].text)
    hindi = int(cells[4].text)
    marathi = int(cells[5].text)
    if english > 60 or hindi > 60 or marathi > 60:
        students_above_60.append((cells[1].text, english, hindi, marathi))

for student in students_above_60:
    if student[1] > toppers['English'][1]:
        toppers['English'] = [student[0], student[1]]
    if student[2] > toppers['Hindi'][1]:
        toppers['Hindi'] = [student[0], student[2]]
    if student[3] > toppers['Marathi'][1]:
        toppers['Marathi'] = [student[0], student[3]]

for subject in toppers:
    print("The topper of %s exam is %s scoring %s marks." %\
            (subject, toppers[subject][0], toppers[subject][1]))

input("Press Enter to Exit...")
driver.quit()
