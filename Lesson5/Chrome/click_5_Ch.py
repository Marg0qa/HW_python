from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = 'https://the-internet.herokuapp.com/add_remove_elements/' # Задайте URL страницы с кнопками

driver = webdriver.Chrome()
driver.get(url) # Откройте страницу
for click in range(5): # Кликните  пять раз
    add_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[onclick="addElement()"]')))
    add_button.click()
delete_buttons = driver.find_elements(By.CSS_SELECTOR,'button[onclick="deleteElement()"]') # Соберите список кнопок Delete
print(len(delete_buttons)) # Выведите размер списка 
sleep(5)
driver.quit() # Закройте браузер