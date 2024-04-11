from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.get("http://uitestingplayground.com/textinput")

input_field = driver.find_element(By.CSS_SELECTOR,'input[id="newButtonName"]') # Находим поле ввода и выполняем шаги
input_field.send_keys("SkyPro")
button = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#updatingButton'))).click()

print(driver.find_element(By.CSS_SELECTOR, '#updatingButton').text )
driver.quit()