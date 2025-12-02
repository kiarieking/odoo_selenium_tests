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

@pytest.mark.order(25)
def test_confirm_creditnote(driver,login,accounting_icon):
    login(EMAIL,PASSWORD)
    accounting_icon()
    group_creditnote(driver)
    status = "Draft"
    invoice_no = "RINV/2025/0016"
    open_creditnote(driver,status,invoice_no)

def group_creditnote(driver):
    customers_btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[normalize-space()='Customers']]")))
    customers_btn.click()
    invoices = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[normalize-space()='Credit Notes']")))
    invoices.click()
    WebDriverWait(driver,15).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//li[contains(@class,'breadcrumb-item') and contains(@class,'active')]//span[normalize-space()='Credit Notes']")
        )
    )

    group_by = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//span[@class='o_dropdown_title' and normalize-space()='Group By']")))
    group_by.click()
    status = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//span[@role='menuitemcheckbox' and normalize-space()='Status']")))
    status.click()

def open_creditnote(driver,status,invoice_no):
    status_xpath = f"//th[@class='o_group_name' and contains(normalize-space(), '{status}')]"
    invoice_grp = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,status_xpath)))
    invoice_grp.click()
    invoice_xpath = f"//td[normalize-space()='{invoice_no}']"

    invoice = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,invoice_xpath)))
    invoice.click()
    time.sleep(3)