from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def test_confirm_post_cancel(driver,login,carrier_icon):
    email = "kelvin.kiarie@quatrixglobal.com"
    password = "$kingara120"
    login(email,password)
    carrier_icon()
    group_orders(driver)
    open_order(driver)
    confirm_order(driver)
    time.sleep(5)

def group_orders(driver):
    group_by = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//i[@class='fa fa-bars']/following-sibling::span[text()='Group By']")))
    group_by.click()
    status = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@aria-checked='false' and @role='menuitemcheckbox' and text()='Status']")))
    status.click()

def open_order(driver):
    quotation = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//th[@class='o_group_name' and contains(., 'Order')]")))
    quotation.click()
    element = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='CO12840'])[1]/following::td[1]")))
    element.click()

def confirm_order(driver):
    # confirm_btn = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME, "action_confirm")))
    # confirm_btn.click()
    status = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//button[@data-value='order']")))
    title = status.get_attribute("title")
    assert title == "Current state"