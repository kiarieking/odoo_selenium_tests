from dotenv import load_dotenv
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def test_create_voucher(driver,login,fuel_icon):
    login(EMAIL,PASSWORD)
    fuel_icon()
    group_vouchers(driver)
    status = "Quotation"
    voucher_no = "FO3930"
    open_voucher(driver,status,voucher_no)


def group_vouchers(driver):
    group_by = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//i[@class='fa fa-bars']/following-sibling::span[text()='Group By']")))
    group_by.click()
    status = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//a[@aria-checked='false' and @role='menuitemcheckbox' and text()='Status']")))
    status.click()

def open_voucher(driver,status,voucher_no):
    status_xpath = f"//th[@class='o_group_name' and contains(., '{status}')]"
    status = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, status_xpath)))
    status.click()
    voucher_xpath = f"(.//*[normalize-space(text()) and normalize-space(.)='{voucher_no}'])[1]/following::td[1]"
    voucher = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, voucher_xpath)))
    voucher.click()
    time.sleep(3)
    