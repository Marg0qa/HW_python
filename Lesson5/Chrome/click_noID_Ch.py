from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url1='http://uitestingplayground.com/dynamicid'

for click in range(3): # Цикл 3 разa
    driver = webdriver.Chrome()
    driver.get(url1)
    button = driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]')
    button.click()
    sleep(3)
    try: #Ожидается появление кнопки 
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-primary"]')))
    except: #Если кнопка не появляется в течение 5 секунд, выбрасывается сообщение, и скрипт сообщает о проблеме.
        print("Кнопка не нажата или не найдена")
    finally:
        driver.quit()