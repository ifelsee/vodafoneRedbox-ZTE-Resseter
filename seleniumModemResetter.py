## Vodafone redbox ZTE modemleri ile uyumludur.
#
#
# https://www.github.com/ifelsee

import sys 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

password = sys.argv[1]
def onOff(cStatus,browser):
    if cStatus == True: 
        browser.find_element(By.ID, "h_connect_btn").click()
        time.sleep(5)
        browser.find_element(By.ID, "h_connect_btn").click()
    else:
        browser.find_element(By.ID, "h_connect_btn").click()


controlL = 0
def login():
    global controlL
    global password
    controlL+=1
    fireFoxOptions = FirefoxOptions()

    ##TODO Makes firefox run in the background
    fireFoxOptions.headless = True 
    browser = webdriver.Firefox(options=fireFoxOptions)

    browser.get('http://192.168.0.1/index.html#login')  #Login Page Url
    try:
        browser.implicitly_wait(5)
        flag1 = True
        while flag1:
            try:
                time.sleep(1)

                browser.find_element(By.ID, "txtPwd").send_keys(password)## Modem Password 
                browser.find_element(By.ID, "btnLogin").click()
                browser.implicitly_wait(3)
                flag1 = False
            except:pass
        time.sleep(2) 
        flag2 = True
        while flag2:
            cStatus = browser.find_element(By.ID, "h_connect_btn").get_attribute("class") 
            cStatus = False if cStatus == "h_connect_off" else True
            try:
                onOff(cStatus, browser)
                flag2 = False
            except:pass
        cStatus = browser.find_element(By.ID, "h_connect_btn").get_attribute("class")
        cStatus = False if cStatus == "h_connect_off" else True

        time.sleep(3)
        browser.quit()
        return cStatus
    except: 
        browser.quit()
        if controlL >1 :
            return 1
        login() 

try:
    login()
except:
    import os
    os.system("rm -rf ./geckodriver.log")
    login()
