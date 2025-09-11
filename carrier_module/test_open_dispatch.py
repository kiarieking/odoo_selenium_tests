from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_open_carrier(login, driver):
    email = "kelvin.kiarie@quatrixglobal.com"
    password = "$kingara120"
    login(email,password)
    carrier_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-menu-xmlid='quatrix_carrier_orders.main_menu']")))
    driver.execute_script("arguments[0].scrollIntoView(true); arguments[0].click();", carrier_btn)
    carrier_btn.click()
    