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

failureArray = []


#tierList = []

#dataframe creation to seperate out price tiers
df = pd.read_csv('PriceTiering.csv')

config = configparser.ConfigParser()
config.read("config.ini")
#init browser

tierList = []

for x in range(9):
    currentTier = 'tier' + str(x+1)
    if config['EditTiers'][currentTier] == "true":
        tierList.append(x+1)
print(tierList)

#init browser

username = config['SectionOne']['UserName']
password = config['SectionOne']['Password']
actualItemNumber = config['SectionOne']['ItemNumber']
chrome_options = webdriver.ChromeOptions()
chrome_driver_service = Service(executable_path = "chromedriver.exe")
chrome_driver_service.start()
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
    element = browser.find_element_by_id('Email')
    element.send_keys(username)
    element2 = browser.find_element_by_id('Password')
    element2.send_keys(password)
    browser.find_element_by_xpath('//*[@class = "button-1 login-button"]').click()

#goes to the menu for tier prices and selects add new record.
def getToMenu():
    browser.find_element_by_link_text("Tier prices").click()
    browser.find_element_by_link_text("Add new record").click()

def selectAnOption(locationName):
    #dropdown menu, need to figure out a way to select options from dropdown menu.
    if locationName == "Mesa":
        locationName = "s "+locationName
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="tierprices-gridform"]/table/tbody/tr[1]/td[1]/div/div').click()
    time.sleep(1)
    parentElement = browser.find_element_by_xpath("//div[@class='t-popup t-group']")
    childElement = parentElement.find_element_by_xpath(".//*[contains(text(),'"+locationName+"')]" )
    childElement.click()

def enterAPrice():
    
    priceEl = browser.find_element_by_id('Price1')
    priceEl.send_keys(priceEntry)
    submitButton = browser.find_element_by_link_text("Insert")
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

            except NoSuchElementException:
                print(setVar + " failed. Retrying...")
                print("This has been tried " + str(tryCounter+1) + " times.")
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
        

credential()
signIn()
for i in tierList:
    tierVar = int(i)

    priceEntry = config["Prices"]['Price'+str(i)]

    newDF=df[df['Price Tier'] == tierVar]
    print(newDF)
    loopF(newDF)

print("Prices were updated for locations in price tier " + str(tierVar))
print("The following locations did not have a price successfully added.")
print(failureArray)
print("Task failed successfully!")

input("Press Enter to exit")
browser.quit()
chrome_driver_service.stop()



exit()


#this is for multi window applications
#browser.find_element_by_xpath('//*[@id="pvav-grid"]/table/tbody/tr[1]/td[11]/input').click()
# window_after = browser.window_handles[1]
# browser.switch_to_window(window_after)
# browser.find_element_by_xpath('//*[@id="product-edit"]/ul/li[2]/a').click()
# browser.find_element_by_xpath('//*[@class = "t-button t-grid-add"]').click()

#WebDriverWait(browser,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="products-grid"]/table/tbody/tr[8]/td[9]/a'))).click()











