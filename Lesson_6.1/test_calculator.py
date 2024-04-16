import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    def quit_driver():
        driver.quit()
    request._schedule_finalizers(quit_driver)
    return driver

def test_slow_calculator(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "#delay"))) # Вводим значение в поле
    delay_input.send_keys("45")

    buttons = ["7", "+", "8", "="] # Нажимаем на кнопки
    for button in buttons:
        driver.find_element_by_xpath(f"//button[text()='{button}']").click()

    WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.CSS_SELECTOR, "result")))  # Ждём 45 секунд и проверяем результат
    result_element = driver.find_element(By.CSS_SELECTOR, "result")
    assert int(result_element.text) == 15
