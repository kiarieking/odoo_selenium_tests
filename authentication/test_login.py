import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def login(driver):
    def _login(email,password):
        driver.get('https://sandbox.erp.quatrixglobal.com/')

        driver.find_element(By.ID, "login").send_keys(email)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'btn-primary')]").click()
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='o_menu_brand' and normalize-space()='Discuss']")))

        assert "Discuss" in driver.page_source
    return _login
    
def test_valid_login(driver, login):
    login("kelvin.kiarie@quatrixglobal.com", "$kingara120")
    assert "Discuss" in driver.page_source

def test_invalid_login(driver, login):
    