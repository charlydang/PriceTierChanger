from os import link
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, select
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
import getpass
import time
import configparser






#inputs


#declared global var

username = "cdang@bjsrestaurants.com"
failureArray = []

#init browser

chrome_driver_service = Service(executable_path = 'C:/Users/cdang/Documents/Scripts/PriceTierChanger2/chromedriver.exe')
chrome_driver_service.start()
config = configparser.ConfigParser()
config.read("config.ini")

actualItemNumber = config['SectionOne']['ItemNumber']

#webdriver path
#init browser
chrome_options = webdriver.ChromeOptions()
#webdriver path
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.headless = False
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
global browser, window_before
browser = webdriver.Chrome(service=chrome_driver_service, options=chrome_options)
browser.get('http://testorder.bjsrestaurants.com/Admin/Product/Edit/'+actualItemNumber)
window_before = browser.window_handles[0]

#PW grab from text file
def credential():
    try:
        with open('test.txt', 'r') as myfile:
            global password
            password = myfile.read().replace('\n','')
    except Exception as error:
        print('Error',error)
    else:
        print('Password Entered')
def passwordDef():
    global password
    try:
        password = getpass.getpass(prompt='Password?')
    except Exception as error:
        print('ERRROR', error)
    else:
        print("Password has been entered", password)
#sign in
def signIn():
    time.sleep(15)
    element = browser.find_element_by_id('Email')
    element.send_keys(username)
    element2 = browser.find_element_by_id('Password')
    element2.send_keys(password)
    browser.find_element_by_xpath('//*[@class = "button-1 login-button"]').click()

#goes to the menu for tier prices and selects add new record.
def getToMenu():
    browser.find_element_by_link_text("Tier prices").click()
    delButton = WebDriverWait(browser,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#tierprices-grid > table > tbody > tr:nth-child(1) > td.t-last > a.t-button.t-grid-delete")))
    delButton.click()
    WebDriverWait(browser,5).until(EC.alert_is_present())
    browser.switch_to.alert.accept()

credential()
signIn()

i = 0
while i == 0:
    time.sleep(1)
    getToMenu()
    browser.refresh()
    WebDriverWait(browser,3).until(EC.visibility_of_any_elements_located)


chrome_driver_service.stop()
