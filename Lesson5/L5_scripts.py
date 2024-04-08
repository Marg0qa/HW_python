
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#1.Клик по кнопке

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


driver2 = webdriver.Firefox()
driver2.get(url) 
for click in range(5): 
    add_button = WebDriverWait(driver2, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[onclick="addElement()"]')))
    add_button.click()
delete_buttons = driver2.find_elements(By.CSS_SELECTOR,'button[onclick="deleteElement()"]') # Соберите список кнопок Delete
print(len(delete_buttons)) # Выведите размер списка 
sleep(5)
driver2.quit() # Закройте браузер

#2.Клик по кнопке без ID 

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

#3 Клик по кнопке с CSS-классом

url_css='http://uitestingplayground.com/classattr'

for click in range(3):
    driver = webdriver.Chrome()
    driver.get(url_css)
    button = driver.find_element(By.CSS_SELECTOR, '.btn-primary')
    button.click()
    try:
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert.accept()
    except TimeoutException:
        print("Alert not present")

    try:
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.loader')))
    except TimeoutException:
        print("Loading indicator still present")
    sleep(3)
    driver.quit()
    sleep(5) #необходимо доп.время ,чтобы не было ошибки


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

#4 Модальное окно

url_modal = 'http://the-internet.herokuapp.com/entry_ad' # Задайте URL страницы с кнопками

driver = webdriver.Chrome()
driver.get(url_modal)
try:
    modal = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "modal")))

    close_button = modal.find_element(By.XPATH, "//div[@id='modal']//p[contains(text(), 'Close')]")# Нажимаем на кнопку "Close"
    close_button.click()
finally:
    driver.quit()


driver2 = webdriver.Firefox()
driver2.get(url_modal) # Откройте страницу
try: #если всплывает модальное окно
    modal = WebDriverWait(driver2, 10).until(EC.visibility_of_element_located((By.ID, "modal")))
    
    close_button = modal.find_element(By.XPATH, "//div[@id='modal']//p[contains(text(), 'Close')]")# Нажимаем на кнопку "Close"
    close_button.click()
finally:
    driver2.quit()

#5 Поле ввода

url_word = "http://the-internet.herokuapp.com/inputs"

driver = webdriver.Chrome()
driver.get(url_word) 
# Находим поле ввода и выполняем шаги
input_field = driver.find_element(By.TAG_NAME,"input")
input_field.send_keys("1000")
sleep(2)
input_field.clear()
input_field.send_keys("999")
sleep(2)
driver.quit()


driver2 = webdriver.Firefox()
driver2.get(url_word) 
input_field = driver2.find_element(By.TAG_NAME,"input")
input_field.send_keys("1000")
sleep(2)
input_field.clear()
input_field.send_keys("999")
sleep(2)
driver2.quit()

#6 Форма авторизации

url_word = "http://the-internet.herokuapp.com/login"

driver = webdriver.Chrome()
driver.get(url_word) 

search_username = driver.find_element(By.CSS_SELECTOR, 'input[id="username"]')
search_username.send_keys('tomsmith')

search_password = driver.find_element(By.CSS_SELECTOR, 'input[id="password"]')
search_password.send_keys('SuperSecretPassword!')

driver.find_element(By.CSS_SELECTOR,'button.radius').click()
sleep(2)
driver.quit()


driver2 = webdriver.Firefox()
driver2.get(url_word) 

search_username = driver2.find_element(By.CSS_SELECTOR, 'input[id="username"]') 
search_username.send_keys('tomsmith')

search_password = driver2.find_element(By.CSS_SELECTOR, 'input[id="password"]') 
search_password.send_keys('SuperSecretPassword!')

driver2.find_element(By.CSS_SELECTOR,'button.radius').click()
sleep(2)
driver2.quit()