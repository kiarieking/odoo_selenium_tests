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
    group_invoices(driver)
    status = "Draft"
    invoice_no = "INV/2023/0844"
    open_invoices(driver,status,invoice_no) 
    confirm_invoice(driver)
    time.sleep(3)

def group_invoices(driver):
    customers_btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[normalize-space()='Customers']]")))
    customers_btn.click()
    invoices = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[normalize-space()='Invoices']")))
    invoices.click()
    WebDriverWait(driver,15).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//li[contains(@class,'breadcrumb-item') and contains(@class,'active')]//span[normalize-space()='Invoices']")
        )
    )

    group_by = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//span[@class='o_dropdown_title' and normalize-space()='Group By']")))
    group_by.click()
    status = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//span[@role='menuitemcheckbox' and normalize-space()='Status']")))
    status.click()

def open_invoices(driver,status,invoice_no):
    status_xpath = f"//th[@class='o_group_name' and contains(normalize-space(), '{status}')]"
    invoice_grp = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,status_xpath)))
    invoice_grp.click()
    invoice_xpath = f"//td[@name='name' and normalize-space()='{invoice_no}']"
    invoice = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,invoice_xpath)))
    invoice.click()

def confirm_invoice(driver):
    confirm_btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[.//span[normalize-space()='Confirm']]")))
    confirm_btn.click()
    time.sleep(2)
    # status = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class,'o_arrow_button') and @data-value='posted']")))
    # title = status.get_attribute("title")
    # assert title == "Current state"
    time.sleep(3)