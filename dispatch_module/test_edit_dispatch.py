from dotenv import load_dotenv
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

load_dotenv()
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

def test_create_dispatch(driver,login,dispatch_icon):
    login(EMAIL,PASSWORD)
    dispatch_icon()
    status = "Quotation"
    dispatch_no = "DO10613"
    group_dispatch(driver)
    open_dispatch(driver,status,dispatch_no)

def group_dispatch(driver):
    group_by = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//i[@class='fa fa-bars']/following-sibling::span[text()='Group By']")))
    group_by.click()
    status = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//a[@aria-checked='false' and @role='menuitemcheckbox' and text()='Status']")))
    status.click()
    # time.sleep(3)


def open_dispatch(driver,status,dispatch_no):
    status_xpath = f"//th[@class='o_group_name' and contains(., '{status}')]"
    status = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, status_xpath)))
    status.click()
    dispatch_xpath = f"(.//*[normalize-space(text()) and normalize-space(.)='{dispatch_no}'])[1]/following::td[1]"
    dispatch = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, dispatch_xpath)))
    dispatch.click()
    # time.sleep(3)

def start_editing_dispatch(driver):
    edit_btn = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Edit']")))
    edit_btn.click()

def add_shipper(driver):
    shipper_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME,"partner_id")))
    shipper_input.click()
    new_shipper = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "KEDA CERAMICS INTERNATIONAL COMPANY LIMITED")))
    new_shipper.click()
    time.sleep(5)

def add_vehicle(driver):
    vehicle_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "vehicle_id")))
    vehicle_input.click()
    new_vehicle = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Mitsubishi/Mitsubishi/ExtraVehicle#1")))
    new_vehicle.click()
    time.sleep(5)




