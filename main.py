from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

s = Service("C://bin/chromedriver.exe")
driver = webdriver.Chrome(service = s)
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

def Add_Remove():
    time.sleep(1) # added sleep function just for better overview
    for num in range(5):
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/button").click()  # adding new buttons //select and copy full xpath on selected button
    time.sleep(2)
    for num in range(4):
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/button[1]").click() # removing new buttons

Add_Remove()

#"/html/body/div[2]/div/div/div/button[1]"
#time.sleep(5)