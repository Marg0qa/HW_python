from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

url_word = "http://the-internet.herokuapp.com/login"

driver2 = webdriver.Firefox()
driver2.get(url_word) 

search_username = driver2.find_element(By.CSS_SELECTOR, 'input[id="username"]') 
search_username.send_keys('tomsmith')

search_password = driver2.find_element(By.CSS_SELECTOR, 'input[id="password"]') 
search_password.send_keys('SuperSecretPassword!')

driver2.find_element(By.CSS_SELECTOR,'button.radius').click()
sleep(2)
driver2.quit()