import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.fixture(scope='session')
def driver():
    service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()
    
@pytest.fixture(scope="session")
def login(driver):
    def _login(email,password):
        driver.get('https://sandbox.erp.quatrixglobal.com/')

        driver.find_element(By.ID, "login").send_keys(email)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'btn-primary')]").click()
    return _login