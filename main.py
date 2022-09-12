from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import random

import time

s = Service("C://bin/chromedriver.exe")
driver = webdriver.Chrome(service = s)

def Add_Remove():
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    time.sleep(1) # added sleep function just for better overview
    for num in range(5):
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/button").click()  # adding new buttons //select and copy full xpath on selected button
    time.sleep(1)
    for num in range(4):
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/button[1]").click() # removing new buttons

def DropDown():
    driver.get("https://the-internet.herokuapp.com/dropdown")
    value = random.randint(2,3)
    driver.find_element(By.XPATH, f"//*[@id='dropdown']/option[{value}]").click() #adding random int in range of 2 and 3 inside value variable


Add_Remove() # 1.Test
DropDown() # 2.Test

#https://the-internet.herokuapp.com/dropdown  //*[@id="dropdown"]/option[3]
#time.sleep(5)