from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url1='http://uitestingplayground.com/dynamicid'

for click in range(3): 
    driver2 = webdriver.Firefox()
    driver2.get(url1)
    button = driver2.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]')
    button.click()
    sleep(3)
    try:
        WebDriverWait(driver2, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-primary"]')))
    except:
        print("Кнопка не нажата или не найдена")
    finally:
        driver2.quit()