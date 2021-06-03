#!/usr/bin/env python3.9
from logging import debug, error, exception, warn
from selenium.webdriver.remote.utils import load_json
from user_agent import generate_user_agent
from platform import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os
import platform
import json
from  random import randint
import sys
from selenium.common.exceptions import NoSuchElementException
from function.web import *
    
path = os.getcwd()+'\\'
options = Options()
#Launch Arguments
useragent = 'User-Agent=' + generate_user_agent(navigator=["chrome", "firefox"])
arguments = [
        '--no-sandbox',
        useragent,
        '--disable-dev-shm-usage',
        '--headless',
        '--log-level=3'
        
]
seperator = '\n'
for obj in arguments: #Load every launch argument
     options.add_argument(obj)
options.add_argument(path)

driver = webdriver.Chrome(options=options, executable_path=execpath)
if platform.system() == 'Windows':
    execpath = "./chromedriver.exe"
#macOS
elif platform.system() == 'Darwin':
    execpath = '/usr/local/bin/chromedriver'
##Linux
elif platform.system() == 'Linux':
    execpath = '/usr/bin/chromedriver'
##None Detected
else:
    raise exception('Insert Here!')

with open('wallets.txt') as w:
    wallet_addresses = list(w)



try:
    for obj in wallet_addresses:
        try:
            def test():
                driver.get('https://safedoge.xyz/index.php')
                driver.find_element(By.CSS_SELECTOR, "#username").send_keys(obj, Keys.RETURN)
                try:
                    balance = driver.find_element(By.XPATH, "/html/body/section[1]/div/div/div[1]/div/h3/input").get_attribute("value")
                except:
                    balance = driver.find_element(By.XPATH, "/html/body/section[1]/div/div/div[1]/div/h3/input").get_attribute("value")
                    pass
                print("Balance: for Address " + obj + ": " + balance + " DOGE")
                driver.get('https://safedoge.xyz/logout.php')
        except NoSuchElementException:
            driver.get('https://safedoge.xyz/logout.php')
            test()
            pass
        except:
            driver.get('https://safedoge.xyz/logout.php')
            test()
            pass
        finally:
            driver.get('https://safedoge.xyz/logout.php')
            test()
            pass
except:
    test()
    pass
        
    
    
if KeyboardInterrupt:
    driver.quit()



