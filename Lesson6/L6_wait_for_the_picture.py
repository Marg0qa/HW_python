from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
driver.implicitly_wait(10)

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//img[@id="landscape"]'))) # Дожидаемся загрузки 4-й картинки
    image_src = driver.find_elements(By.CSS_SELECTOR, 'img')[-2].get_attribute("src") # Получаем значение атрибута src у 3-й картинки
    print(image_src)
    
finally:
    driver.quit()