import pytest
import colorlover
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

@pytest.fixture(scope="module")
def init_driver(request): # Функция для инициализации драйвера
    driver = webdriver.Chrome()  # Замените на Ваш веб-драйвер
    request.instance.driver = driver
    yield driver
    driver.quit()
    
print("start")

def test_fill_form(driver):
    driver.get(url)
    
    first_name = driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]') 
    first_name.send_keys('Иван')
    
    last_name = driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]') 
    last_name.send_keys('Петров')
    
    address = driver.find_element(By.CSS_SELECTOR, 'input[name="address"]') 
    address.send_keys('Ленина, 55-3')
    
    zip_code = driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]') 
    zip_code.send_keys('')
    
    city = driver.find_element(By.CSS_SELECTOR, 'input[name="city"]') 
    city.send_keys('Москва')
    
    country = driver.find_element(By.CSS_SELECTOR, 'input[name="country"]') 
    country.send_keys('Россия')
    
    email = driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]') 
    email.send_keys('test@skypro.com')
    
    phone = driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]') 
    phone.send_keys('+7985899998787')
    
    job_position = driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]') 
    job_position.send_keys('QA')
    
    company = driver.find_element(By.CSS_SELECTOR, 'input[name="company"]') 
    company.send_keys('SkyPro')
    
    #  element.style  .alert-success{background-color: #d1e7dd;}-green      .alert-danger {background-color: #f8d7da;}-red
    
    button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    
@pytest.mark.usefixtures("init_driver")
class TestZipCodeHighlight:
    def test_zip_code_highlight(self):
        
        zip_code_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "zip_code")))
        assert zip_code_field.value_of_css_property('border-color') == 'rgb(255, 0, 0)' # Проверяем, подсвечено ли поле Zip code красным
        
        other_fields = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="text"]:not([name="zip_code"])')
        for field in other_fields:
            assert field.value_of_css_property('border-color') == 'rgb(0, 255, 0)' # Проверяем, подсвечены ли остальные поля зеленым
print("stop")
# try:
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="zip-code"].error')))
#     zip_code = True
# except TimeoutException:
#     zip_code = False
    
# for selector in ['input[name="first-name"]', 'input[name="last-name"]', 'input[name="address"]', 'input[name="city"]', 'input[name="country"]', 
# 'input[name="e-mail"]', 'input[name="phone"]', 'input[name="job-position"]', 'input[name="company"]']:
#         try:
#             WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, f'{selector}.success')))
#         except TimeoutException:
#             assert False, f"{selector} поле не выделено зеленым"
# assert zip_code, "Поле Zip code не выделен красным"

# if __name__ == "__main__":
#     pytest.main()

# try:
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="zip-code"].error')))
#     zip_code = True
# except TimeoutException:
#     zip_code = False, "Поле не выделено зеленым"

# for selector in ['input[name="first-name"]', 'input[name="last-name"]', 'input[name="address"]', 'input[name="city"]', 'input[name="country"]', 'input[name="e-mail"]', 'input[name="phone"]', 'input[name="job-position"]', 'input[name="company"]']:
#     try:
#         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
#     except TimeoutException:
#             assert False, f"{selector} field is not highlighted green"
# def test_color(self, first_name, last_name, address, zip_code, city, country, email, phone, job_position, company)
