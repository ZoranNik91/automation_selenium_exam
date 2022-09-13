from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from array import *
import string
import random
import shutil
import requests
import time

import urllib.request
import base64

s = Service("C://bin/chromedriver.exe")
driver = webdriver.Chrome(service = s)

# def Add_Remove(): #1
#     driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
#     time.sleep(1) # added sleep function just for better overview
#     for i in range(5):
#         driver.find_element(By.XPATH,"/html/body/div[2]/div/div/button").click()  # adding new buttons //select and copy full xpath on selected button
#     time.sleep(1)
#     for i in range(4):
#         driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/button[1]").click() # removing new buttons
#     time.sleep(1)
#
# def DropDown(): #2
#     driver.get("https://the-internet.herokuapp.com/dropdown")
#     value = random.randint(2,3)
#     driver.find_element(By.XPATH, f"//*[@id='dropdown']/option[{value}]").click() #adding random int in range of 2 and 3 inside value variable
#     time.sleep(1)
#
# def Dynamic(): #3
#     driver.get("https://the-internet.herokuapp.com/dynamic_content")
#     wait = WebDriverWait(driver, 10)
#     img_list = []
#     for i in range(10):
#         l1 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div/div[1]/div[1]/img"))).get_attribute("src") # 1.image
#         img_list.append(l1)
#         l2 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div[1]/img"))).get_attribute("src") # 2.image
#         img_list.append(l2)
#         l3 = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div/div[3]/div[1]/img"))).get_attribute("src") # 3.image
#         img_list.append(l3)
#         if(i==9):
#             [print(img_list.count(x), x) for x in set(img_list)]
#         driver.refresh()
#
# def Alerts():
#     driver.get("https://the-internet.herokuapp.com/javascript_alerts")
#     wait = WebDriverWait(driver, 10)
#     letters = string.ascii_letters
#     random_string = ''.join(random.choice(letters) for i in range(10))
#
#     driver.find_element(By.XPATH, "/html/body/div[2]/div/div/ul/li[1]/button").click() #JS ALert button
#     wait.until(EC.alert_is_present())
#     time.sleep(1)
#     driver.switch_to.alert.accept()
#
#     driver.find_element(By.XPATH, "/html/body/div[2]/div/div/ul/li[2]/button").click() #JS Confirm button
#     wait.until(EC.alert_is_present())
#     time.sleep(1)
#     driver.switch_to.alert.dismiss()
#
#     driver.find_element(By.XPATH, "/html/body/div[2]/div/div/ul/li[3]/button").click()  # JS Prompt button
#     wait.until(EC.alert_is_present())
#     driver.switch_to.alert.send_keys(random_string)
#     time.sleep(1)
#     driver.switch_to.alert.accept()
#     time.sleep(1)

def DOM():
    driver.get("https://the-internet.herokuapp.com/challenging_dom")
    canv = driver.find_element(By.XPATH, '//*[@id="content"]/script').get_attribute("textContent") #delete -> /text() to fix the error (element is not an object)
    print("-----------------------------------")
    print(canv)


    # action = ActionChains(driver)
    # action.context_click(img).perform()

    # driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[1]/a[1]").click()  # qux button
    # driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[1]/a[2]").click()  # buz ALert button
    # driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[1]/a[3]").click()  # bar ALert button
    # driver.get("https://www.ocr2edit.com/convert-to-txt")
    # driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div[1]/div[1]/div/div/button").send_keys("C://Users/ZOHAN/Downloads/download.png")

# Add_Remove()#1.Test
# DropDown()  #2.Test
# Dynamic()   #3.Test
# Alerts()    #4.Test
DOM()         #5.test

# https://the-internet.herokuapp.com/javascript_alerts
#time.sleep(5)