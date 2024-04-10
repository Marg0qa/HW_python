from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url_modal = 'http://the-internet.herokuapp.com/entry_ad' # Задайте URL страницы с кнопками

driver = webdriver.Chrome()
driver.get(url_modal)
try:
    modal = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "modal")))

    close_button = modal.find_element(By.XPATH, "//div[@id='modal']//p[contains(text(), 'Close')]")# Нажимаем на кнопку "Close"
    close_button.click()
finally:
    driver.quit()