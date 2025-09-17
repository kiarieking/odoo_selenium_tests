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
    open_new_dispatch(driver)
    add_shipper(driver)
    add_vehicle(driver)
    
def open_new_dispatch(driver):
    create_btn = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//button[.//span[normalize-space(text())='Create']]")))
    create_btn.click()
    time.sleep(3)

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

def add_product_line(driver):
    add_line = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Add a line")))
    add_line.click()
    product_input = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME, "product_id")))
    product_input.click()
    product = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT, "[KEDA] CHAVAKALI 28T")))
    product.click()






    
