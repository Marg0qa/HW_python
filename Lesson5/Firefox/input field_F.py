
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

url_word = "http://the-internet.herokuapp.com/inputs"

driver2 = webdriver.Firefox()
driver2.get(url_word) 
input_field = driver2.find_element(By.TAG_NAME,"input")
input_field.send_keys("1000")
sleep(2)
input_field.clear()
input_field.send_keys("999")
sleep(2)
driver2.quit()
