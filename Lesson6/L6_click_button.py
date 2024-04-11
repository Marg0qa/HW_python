from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.implicitly_wait(20)
driver.get("http://uitestingplayground.com/ajax")

button = driver.find_element(By.CSS_SELECTOR, '.btn-primary').click() # Нажатие на кнопку

wait = WebDriverWait(driver, 10) # Ожидание загрузки данных
green_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success")))
text = green_box.text

print(text)
driver.quit()

