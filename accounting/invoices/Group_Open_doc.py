from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class Group_Open_doc:
    def __init__(self):
        pass

    def group_by(self,driver):
        customers_btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[normalize-space()='Customers']]")))
        customers_btn.click()
        invoices = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[normalize-space()='Invoices']")))
        invoices.click()
        WebDriverWait(driver,15).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//li[contains(@class,'breadcrumb-item') and contains(@class,'active')]//span[normalize-space()='Invoices']")
            )
        )

        group_by_btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//span[@class='o_dropdown_title' and normalize-space()='Group By']")))
        group_by_btn.click()
        status = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//span[@role='menuitemcheckbox' and normalize-space()='Status']")))
        status.click()
