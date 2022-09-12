from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import random
from array import *

import time

s = Service("C://bin/chromedriver.exe")
driver = webdriver.Chrome(service = s)

def Add_Remove(): #1
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    time.sleep(1) # added sleep function just for better overview
    for num in range(5):
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/button").click()  # adding new buttons //select and copy full xpath on selected button
    time.sleep(1)
    for num in range(4):
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/button[1]").click() # removing new buttons

def DropDown(): #2
    driver.get("https://the-internet.herokuapp.com/dropdown")
    value = random.randint(2,3)
    driver.find_element(By.XPATH, f"//*[@id='dropdown']/option[{value}]").click() #adding random int in range of 2 and 3 inside value variable
    time.sleep(1)

def Dynamic(): #3
    driver.get("https://the-internet.herokuapp.com/dynamic_content")
    for num in range(10):
        print(driver.findElement(By.XPATH("/html/body/div[2]/div/div/div/div/div[1]/div[1]/img")).get_attribute('src'))
        #l2 = driver.findElement(By.XPATH("/html/body/div[2]/div/div/div/div/div[1]/div[2]/img")).get_attribute('src')
        #l3 = driver.findElement(By.XPATH("/html/body/div[2]/div/div/div/div/div[1]/div[3]/img")).get_attribute('src')

        driver.refresh()



Add_Remove() #1.Test
DropDown() #2.Test
Dynamic() #3.Test

#for i in array:    print(array[i], end=" ")
#time.sleep(5)