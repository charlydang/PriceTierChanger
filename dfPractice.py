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

#dataframe creation to seperate out checked sites vs unchecked sites
df = pd.read_csv('LocationsCheck.csv')

needCheckSites = df[df['Check'] == 1]
needUncheckSites = df[df['Check'] == 0]

print("Sites that need to check")
for index, row in needCheckSites.iterrows():
    print(row['Value'])
