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
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
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
chrome_driver_service = Service(executable_path = 'C:/Users/cdang/Documents/Scripts/PriceTierChanger2/chromedriver.exe')
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
    element = browser.find_element(By.ID, 'Email')
    element.send_keys(username)
    element2 = browser.find_element(By.ID, 'Password')
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

        browser.find_element(By.XPATH, "//input[@value='Save']").click()
    except Exception as error:
        print('Error',error)

def LocationCheckBoxRun():
    browser.get('http://testorder.bjsrestaurants.com/Admin/Product/Edit/'+actualItemNumber)
    window_before = browser.window_handles[0]

    signIn()
    getToLocations()

    needCheckSites = df[df['Check'] == 1]
    needUncheckSites = df[df['Check'] == 0]
    print(needCheckSites)
    print(needUncheckSites)
    for index, row in needCheckSites.iterrows():
    
        checkLocations(str(row['Value']))

    for index, row in needUncheckSites.iterrows():
    
        unCheckLocations(str(row['Value']))
    saveLocations()
    #input("Press Enter to exit")
    time.sleep(8)
    browser.quit()
    chrome_driver_service.stop()
    config['SectionOne']['Password'] = ""
    with open('config.ini', 'w') as configfile:    # save
        config.write(configfile)        
            
    exit()

LocationCheckBoxRun()


#checkLocations("10")
#checkLocations("100")






# loopF(newDF)

#print("Prices were updated for locations in price tier " + str(tierVar))
#print("The following locations did not have a price successfully added.")
#print(failureArray)
#print("Task failed successfully!")




#this is for multi window applications
#browser.find_element_by_xpath('//*[@id="pvav-grid"]/table/tbody/tr[1]/td[11]/input').click()
# window_after = browser.window_handles[1]
# browser.switch_to_window(window_after)
# browser.find_element_by_xpath('//*[@id="product-edit"]/ul/li[2]/a').click()
# browser.find_element_by_xpath('//*[@class = "t-button t-grid-add"]').click()

#WebDriverWait(browser,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="products-grid"]/table/tbody/tr[8]/td[9]/a'))).click()











