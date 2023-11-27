from os import link
from tokenize import String
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, select
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

import csv
import getpass
import time
import configparser

#inputs

#declared global var

#dataframe creation to seperate out price tiers
df = pd.read_csv('LocationsCheck.csv')

config = configparser.ConfigParser()
config.read("config.ini")

username = config['SectionOne']['UserName']
password = config['SectionOne']['Password']
actualItemNumber = config['SectionOne']['ItemNumber']
chrome_options = webdriver.ChromeOptions()
chrome_driver_service = Service(executable_path = 'chromedriver.exe')
chrome_driver_service.start()
#webdriver path
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.headless = False
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

global browser, window_before
browser = webdriver.Chrome(service=chrome_driver_service, options=chrome_options)






#sign in
def signIn():
    element = browser.find_element("id", 'Email')
    element.send_keys(username)
    element2 = browser.find_element("id", 'Password')
    element2.send_keys(password)
    browser.find_element(By.XPATH, '//*[@class = "button-1 login-button"]').click()


#goes to the menu for tier prices and selects add new record.
def getToLocations():
    browser.find_element(By.LINK_TEXT, "Locations").click()

#Selects the locations if they have a 1 next to their name
def checkLocations (siteValue):
    try:
        print("Finding value at"+siteValue)
        if not browser.find_element(By.XPATH, "//input[@value="+siteValue+" and @type='checkbox']").is_selected():
            browser.find_element(By.XPATH, "//input[@value="+siteValue+" and @type='checkbox']").click()
    except Exception as error:
        print('Error',error)

#Uncheck the locations that have a 0 next to their name.
def unCheckLocations (siteValue):
    try:
        print("Finding value at"+siteValue)
        if browser.find_element(By.XPATH, "//input[@value="+siteValue+" and @type='checkbox']").is_selected():
            browser.find_element(By.XPATH, "//input[@value="+siteValue+" and @type='checkbox']").click()
    except Exception as error:
        print('Error',error)
        
def saveLocations():
    time.sleep(2)
    try:

        browser.find_element_(By.XPATH, "//input[@value='Save']").click()
    except Exception as error:
        print('Error',error)


def findName (inputValue):
    matches = browser.find_elements(By.XPATH, "//*[@id='pnl-available-stores']/td[2]/div["+str(inputValue)+"]")
    return matches[0].text

def LocationCheckBoxRun():
    browser.get('http://testorder.bjsrestaurants.com/Admin/Product/Edit/'+actualItemNumber) #http://testorder.bjsrestaurants.com/Admin/Store/List')
    window_before = browser.window_handles[0]

    signIn()

    #table_id = browser.find_element(By.XPATH, '//*[@id="stores-grid"]/table')
    #rows = table_id.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
    #print('HERE' + rows)
    #for row in rows:
    #    # Get the columns (all the column 2)        
    #    col = row.find_elements(By.TAG_NAME, "td")[0] #note: index start from 0, 1 is col 2
    #    print(col)

    getToLocations()
    time.sleep(8)
    column1 = []
    column2 = []
    


    for x in range(2, 999):
        try:
            if (findName(x) != "None"):
                #print(findName(x))
                column1.append(findName(x))
        except Exception as error:
            print(error)
            break

    #GETS THE ID VALUES OF SITES
    #counter = 0
    grid = browser.find_elements(By.NAME, "SelectedStoreIds")
    for g in grid:
        #print('Site Value: ' + g.get_attribute('value') )
        column2.append(g.get_attribute('value'))
        

    
    header = ['Check', 'Value', 'Location'] 


    wtr = csv.writer(open ('PriceTieringNEW.csv', 'w'), delimiter=',', lineterminator='\n')
    wtr.writerow(header)
    for x in range(0, len(column1)) : wtr.writerow ([0,column2[x],column1[x]])

    time.sleep(8)
    browser.quit()
    chrome_driver_service.stop()
    config['SectionOne']['Password'] = ""
    with open('config.ini', 'w') as configfile:    # save
        config.write(configfile)        
            
    exit()



LocationCheckBoxRun()



