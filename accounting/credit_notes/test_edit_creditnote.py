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

def test_edit_creditnote(driver,login,accounting_icon):
    login(EMAIL,PASSWORD)
    accounting_icon()
    group_creditnote(driver)
    status = "Draft"
    open_creditnote(driver,status)
    edit_credit_note(driver)
    time.sleep(5)

def group_creditnote(driver):
    customers_btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[normalize-space()='Customers']]")))
    customers_btn.click()
    credit_note = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[normalize-space()='Credit Notes']")))
    credit_note.click()
    WebDriverWait(driver,15).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//li[contains(@class,'breadcrumb-item') and contains(@class,'active')]//span[normalize-space()='Credit Notes']")
        )
    )

    group_by = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//span[@class='o_dropdown_title' and normalize-space()='Group By']")))
    group_by.click()
    status = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//span[@role='menuitemcheckbox' and normalize-space()='Status']")))
    status.click()

def open_creditnote(driver,status):
    status_xpath = f"//th[@class='o_group_name' and contains(normalize-space(), '{status}')]"
    credit_note_grp = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,status_xpath)))
    credit_note_grp.click()
    wait = WebDriverWait(driver, 20)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//tbody//tr[contains(@class,'o_data_row')]")
        )
    )

    first_credit_note_xpath = (
        "(//tbody//tr[contains(@class,'o_data_row')]"
        "//td[@name='name'])[1]"
    )

    # WAIT: element is visibfrom selenium.webdriver.common.keys import Keysle (NOT clickable)
    credit_note = wait.until(
        EC.visibility_of_element_located((By.XPATH, first_credit_note_xpath))
    )
    credit_note.click()

def edit_credit_note(driver):
    edit_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'o_form_button_edit') and @title='Edit record']")))
    edit_btn.click()
    customer = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@type='text' and contains(@class,'ui-autocomplete-input')]")))
    customer.click()
    select_customer = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(@class,'ui-menu-item-wrapper') and normalize-space()='IN MOTION REGIONAL LOGISTICS LIMITED']")))
    select_customer.click()
    payment_reference = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[contains(@class,'o_field_char') and @name='payment_reference']")))
    payment_reference.click()
    payment_reference.clear()
    payment_reference.send_keys("INV/2023/0844")
    save_btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Save']")))
    save_btn.click()
    
