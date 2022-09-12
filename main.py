from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import random
from array import *
import time

s = Service("C://bin/chromedriver.exe")
driver = webdriver.Chrome(service = s)

def Add_Remove(): #1
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    time.sleep(1) # added sleep function just for better overview
    for i in range(5):
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/button").click()  # adding new buttons //select and copy full xpath on selected button
    time.sleep(1)
    for i in range(4):
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/button[1]").click() # removing new buttons
    time.sleep(1)

def DropDown(): #2
    driver.get("https://the-internet.herokuapp.com/dropdown")
    value = random.randint(2,3)
    driver.find_element(By.XPATH, f"//*[@id='dropdown']/option[{value}]").click() #adding random int in range of 2 and 3 inside value variable
    time.sleep(1)

def Dynamic(): #3
    driver.get("https://the-internet.herokuapp.com/dynamic_content")
    wait = WebDriverWait(driver, 10)
    img_list = []
    for i in range(10):
        l1 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div/div[1]/div[1]/img"))).get_attribute("src") # 1.image
        img_list.append(l1)
        l2 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div[1]/img"))).get_attribute("src") # 2.image
        img_list.append(l2)
        l3 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div/div[3]/div[1]/img"))).get_attribute("src") # 3.image
        img_list.append(l3)
        if(i==9):
            [print(img_list.count(x), x) for x in set(img_list)]
        driver.refresh()

def Alerts():
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/ul/li[1]/button").click() #JS ALert button
    wait.until(EC.alert_is_present())
    time.sleep(1)
    driver.switch_to.alert.accept()

    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/ul/li[2]/button").click() #JS Confirm button
    wait.until(EC.alert_is_present())
    time.sleep(1)
    driver.switch_to.alert.dismiss()

    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/ul/li[3]/button").click()  # JS Prompt button
    wait.until(EC.alert_is_present())
    driver.switch_to.alert.send_keys("Send Nudes")
    time.sleep(1)
    driver.switch_to.alert.accept()

Add_Remove()#1.Test
DropDown()  #2.Test
Dynamic()   #3.Test
Alerts()    #4.Test

# https://the-internet.herokuapp.com/javascript_alerts
#time.sleep(5)