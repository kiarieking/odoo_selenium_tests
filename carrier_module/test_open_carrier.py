from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_open_carrier(login, driver, carrier_icon):
    email = "kelvin.kiarie@quatrixglobal.com"
    password = "$kingara120"
    login(email,password)
    carrier_icon()
    