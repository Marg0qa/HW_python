from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



url = 'https://the-internet.herokuapp.com/add_remove_elements/'

driver2 = webdriver.Firefox()
driver2.get(url) 
for click in range(5): 
    add_button = WebDriverWait(driver2, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[onclick="addElement()"]')))
    add_button.click()
delete_buttons = driver2.find_elements(By.CSS_SELECTOR,'button[onclick="deleteElement()"]') 
print(len(delete_buttons)) 
sleep(5)
driver2.quit()
