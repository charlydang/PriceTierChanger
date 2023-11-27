#Script by Alex Quan
#Version 1.0
#Known Issues - Exceptions due to Unexpected Error (if item is already added) still occur and break the application
#WORKAROUND - Delete all items in that price tier and try again.
#PT 6 Broken?

from os import link
import pandas as pd
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, select
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
import time
import configparser



warnings.filterwarnings("ignore",category=DeprecationWarning)
    

print("Welcome to the Price Tier Changer...")



failureArray = []


#dataframe creation to seperate out price tiers
df = pd.read_csv('PriceTiering.csv')


#reads config.ini
config = configparser.ConfigParser()
config.read("config.ini")
username = config['SectionOne']['UserName']
password = config['SectionOne']['Password']
actualItemNumber = config['SectionOne']['AttributeID']
sideItemNumber = config['SectionOne']['SideItemNumber']

tierList = []

for x in range(9):
    currentTier = 'tier' + str(x+1)
    if config['EditTiers'][currentTier] == "true":
        tierList.append(x+1)
print(tierList)



print("Changing price for item with attribute ID " + actualItemNumber)
print("This is for side item with attribute ID "+sideItemNumber)
#init browser
chrome_options = webdriver.ChromeOptions()
chrome_driver_service = Service(executable_path = "chromedriver.exe")
chrome_driver_service.start()
#webdriver path
prefs = {"profile.default_content_setting_values.notifications": 2}
#chrome_options.set_capability("UNEXPECTED_ALERT_BEHAVIOR", "ACCEPT")

chrome_options.set_capability('unhandledPromptBehavior', 'accept')
#chrome_options.set_capability("unexpectedAlertBehavior", "accept")
#chrome_options.set_capability("CapabilityType.UNEXPECTED_ALERT_BEHAVIOR", "ACCEPT")

chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.headless = False
global browser, window_before
browser = webdriver.Chrome(service=chrome_driver_service, options=chrome_options)
browser.get('http://testorder.bjsrestaurants.com/Admin/Product/EditAttributeValues?productVariantAttributeId='+actualItemNumber)
window_before = browser.window_handles[0]





#sign in, enters username from config and then asks for user input before continuing.

#sign in
def signIn():
    element = browser.find_element(By.ID, 'Email')
    element.send_keys(username)
    element2 = browser.find_element(By.ID, 'Password')
    element2.send_keys(password)
    browser.find_element(By.XPATH, '//*[@class = "button-1 login-button"]').click()

    
def getToMenu():
    #goes to the menu for tier prices and selects add new record.
    WebDriverWait(browser,3).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Tier prices')))
    browser.find_element(By.LINK_TEXT, "Tier prices").click()
    browser.find_element(By.LINK_TEXT, "Add new record").click()

def selectAnOption(locationName):
    #dropdown menu, need to figure out a way to select options from dropdown menu.
    WebDriverWait(browser,3).until(EC.visibility_of_any_elements_located)
    browser.find_element(By.XPATH, '//*[@id="tierprices-gridform"]/table/tbody/tr[1]/td[1]/div/div').click()
    time.sleep(1)
    parentElement = browser.find_element(By.XPATH, "//div[@class='t-popup t-group']")
    childElement = parentElement.find_element(By.XPATH, ".//*[contains(text(),'"+locationName+"')]" )
    childElement.click()

def enterAPrice():
    #enters the price
    priceEl = browser.find_element(By.ID, 'Price1')
    priceEl.send_keys(priceEntry)
    submitButton = browser.find_element(By.LINK_TEXT, "Insert")
    submitButton.click()

def loopF(thisDF):
    
    #this for loop to loop through the values to give each location the correct price.
    for i in range(len(thisDF)):
        looper = 0
        tryCounter = 0
        while looper == 0:
            try:
                setVar = thisDF.iloc[i,0]
                print("Setting price for "+setVar)
                getToMenu()
                selectAnOption(setVar) 
            except UnexpectedAlertPresentException:
                browser.switch_to.alert.accept()
                
                
                print(setVar + "failed. Retrying...")
                tryCounter+=1
                if tryCounter == 2:
                    print("Something wrong with this location, please manually check")
                    failureArray.append(setVar)
                    looper+=1
                    browser.refresh()
                pass
            except NoSuchElementException:
                print(setVar + " failed. Retrying...")
                print("This has been tried " + str(tryCounter) + " times.")
                tryCounter +=1
                if tryCounter == 3:
                    print("Something wrong with this location, please manually check it.")
                    failureArray.append(setVar)
                    browser.refresh()
                    WebDriverWait(browser,3).until(EC.visibility_of_any_elements_located)
                    looper+=1
                pass
            else:
                try:
                    enterAPrice()
                    browser.refresh()
                except Exception:
                    #does not work, basically fails right now when the location's already been done.
                    print("Did you already finish this location? Please check it")
                    failureArray.append(setVar)
                    browser.switch_to.alert.accept()
                    browser.refresh()
                    looper+=1
                    continue
                    
                else:
                    WebDriverWait(browser,3).until(EC.visibility_of_any_elements_located)
                    looper+=1
                    continue
        
        
def indItemButton(individualItemNumber):
    #opens the individual item to add prices
    browser.execute_script("OpenWindow('/Admin/Product/ProductAttributeValueEditPopup/"+individualItemNumber+"?btnId=btnRefresh&amp;formId=productvariantattribute-form', 800, 500, true)")
    window_after = browser.window_handles[1]
    browser.switch_to.window(window_after)



signIn()
indItemButton(sideItemNumber)
getToMenu()

for i in tierList:
    tierVar = int(i)

    priceEntry = config["Prices"]['Price'+str(i)]

    newDF=df[df['Price Tier'] == tierVar]
    print(newDF)
    loopF(newDF)
print("Pricing added for price tier " + str(tierList))
print("The following locations did not have a price successfully added.")
print(failureArray)
chrome_driver_service.stop()
print("Task failed successfully!")

input("Press Enter to exit")
browser.quit()
exit()









