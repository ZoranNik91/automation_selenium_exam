from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

s = Service("C://bin/chromedriver.exe")
driver = webdriver.Chrome(service = s)
#https://orteil.dashnet.org/cookieclicker/  https://the-internet.herokuapp.com/add_remove_elements/
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/button").click() #select and copy full xpath on selected button

#driver.find_element(By.ID,"langSelect-EN").click()

#time.sleep(5)