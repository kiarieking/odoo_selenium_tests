import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

@pytest.mark.order(18)
def test_confirm_invoice(driver,login,accounting_icon):
    login(EMAIL,PASSWORD)
    accounting_icon()
    customers_btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[normalize-space()='Customers']]")))
    customers_btn.click()
    time.sleep(3)