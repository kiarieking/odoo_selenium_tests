import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope='session')
def driver():
    service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()
    
