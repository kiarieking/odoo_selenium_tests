from dotenv import load_dotenv
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

load_dotenv()
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

def test_create_dispatch(driver,login,dispatch_icon):
    login(EMAIL,PASSWORD)
    dispatch_icon()
    open_new_dispatch(driver)
    
def open_new_dispatch(driver):
    create_btn = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//button[.//span[normalize-space(text())='Create']]")))
    create_btn.click()
    time.sleep(3)




    
