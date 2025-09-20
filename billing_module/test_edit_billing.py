from dotenv import load_dotenv
import os
import time

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def test_edit_billing(driver,login,billing_icon):
    login(EMAIL,PASSWORD)
    billing_icon()
    time.sleep(2)
    