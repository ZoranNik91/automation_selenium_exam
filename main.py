from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

s = Service("C://bin/chromedriver.exe")
driver = webdriver.Chrome(service = s)
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

def Add_Remove():
    for num in range(5):
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/button").click()  # select and copy full xpath on selected button

Add_Remove()
#driver.find_element(By.ID,"langSelect-EN").click()

#time.sleep(5)