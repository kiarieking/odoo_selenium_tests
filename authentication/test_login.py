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
    return _login


def logout(driver):
    driver.get('https://sandbox.erp.quatrixglobal.com/')
    usermenu = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.oe_topbar_name")))
    usermenu.click()
    driver.find_element(By.XPATH, "//a[@data-menu='logout']").click()

    
    
def test_valid_login(driver, login):
    login("kelvin.kiarie@quatrixglobal.com", "$kingara120")
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='o_menu_brand' and normalize-space()='Discuss']")))
    assert "Discuss" in driver.page_source
    logout(driver)
    
def test_invalid_login(driver, login):
    login("test123432@email.com", "pwd123")
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "p.alert.alert-danger[role='alert']")))
    assert "Wrong login/password" in driver.page_source 
    
   