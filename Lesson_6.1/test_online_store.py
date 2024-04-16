import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    yield driver
    driver.quit()

def test_shopping_cart(driver):
    driver.get('https://www.saucedemo.com/') # Открыть сайт магазина

    driver.find_element(By.CSS_SELECTOR, 'input[id="user-name"]').send_keys('standard_user') # Авторизоваться как пользователь standard_user
    driver.find_element(By.CSS_SELECTOR, 'input[id="password"]').send_keys('secret_sauce')
    driver.find_element(By.CSS_SELECTOR, 'input[id="login-button"]').click()

    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click() # Добавить товары в корзину
    driver.find_elements(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
    
    driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container').click() # Перейти в корзину

    driver.find_element(By.CSS_SELECTOR, '#checkout').click() # Нажать Checkout

    driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys('Margarita')# Заполнить форму своими данными
    driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Kulkova')
    driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('196244')

    driver.find_element(By.CSS_SELECTOR, '#continue').click() # Нажать кнопку Continue

    
    total_price = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'summary_total_label'))) # Прочитать со страницы итоговую стоимость (Total)
    assert total_price.text == '$58.29'

    