from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

url_css='http://uitestingplayground.com/classattr'

for _ in range(3): # Элемент постоянно меняет местоположени
    driver2 = webdriver.Firefox()
    driver2.get(url_css)
    button = driver2.find_element(By.CSS_SELECTOR, '.btn-primary')
    button.click()

    try:
        alert = WebDriverWait(driver2, 10).until(EC.alert_is_present())
        alert.accept()
    except TimeoutException:
        print("Alert not present")

    try:
        WebDriverWait(driver2, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.loader')))
    except TimeoutException:
        print("Loading indicator still present")
    sleep(5)
    driver2.quit()