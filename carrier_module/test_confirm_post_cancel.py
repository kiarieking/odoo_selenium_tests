from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# def test_confirm_order(driver,login,carrier_icon):
#     email = "kelvin.kiarie@quatrixglobal.com"
#     password = "$kingara120"
#     status = "Quotation"
#     carrier_no = "CO12835"
#     login(email,password)
#     carrier_icon()
#     group_orders(driver)
#     open_order(driver,status,carrier_no)
#     confirm_order(driver)
#     time.sleep(5)

# def test_post_order(driver,login,carrier_icon):
#     email = "kelvin.kiarie@quatrixglobal.com"
#     password = "$kingara120"
#     status = "Order"
#     carrier_no = "CO12840"
#     login(email,password)
#     carrier_icon()
#     group_orders(driver)
#     open_order(driver,status,carrier_no)
#     post_order(driver)
#     time.sleep(3)

def test_cancel_order(driver,login,carrier_icon):
    email = "kelvin.kiarie@quatrixglobal.com"
    password = "$kingara120"
    status = "Posted"
    carrier_no = "CO12840" 
    login(email,password)
    carrier_icon()
    group_orders(driver)
    open_order(driver,status,carrier_no)
    cancel_order(driver)
    time.sleep(1)

def group_orders(driver):
    group_by = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//i[@class='fa fa-bars']/following-sibling::span[text()='Group By']")))
    group_by.click()
    status = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@aria-checked='false' and @role='menuitemcheckbox' and text()='Status']")))
    status.click()

def open_order(driver,status,carrier_no):
    status_xpath = f"//th[@class='o_group_name' and contains(., '{status}')]"
    quotation = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, status_xpath)))
    quotation.click()
    order_xpath = f"(.//*[normalize-space(text()) and normalize-space(.)='{carrier_no}'])[1]/following::td[1]"
    element = WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH, order_xpath)))
    element.click()

def confirm_order(driver):
    confirm_btn = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME, "action_confirm")))
    confirm_btn.click()
    time.sleep(2)
    status = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//button[@data-value='order']")))
    title = status.get_attribute("title")
    assert title == "Current state"

def post_order(driver):
    post_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "action_post")))
    post_btn.click()
    time.sleep(2)
    status = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@data-value='posted']")))
    title = status.get_attribute("title")
    assert title == "Current state"

def cancel_order(driver):
    cancel_btn = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME, "action_cancel")))
    cancel_btn.click()
    time.sleep(2)
    status = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//button[@data-value='cancel']")))
    title = status.get_attribute("title")
    assert title == "Current state"
