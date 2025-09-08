from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get("https://sandbox.erp.quatrixglobal.com/web")
print(driver.title)