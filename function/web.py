#!/usr/bin/env python3.9
from logging import debug, error, exception, warn
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
path = os.getcwd()+'\\'
"""with open ('././config.json') as config_file:
    config = json.load(config_file)"""
options = Options()
useragent = 'User-Agent=' + generate_user_agent(navigator=["chrome", "firefox"])
arguments = [
        '--no-sandbox',
        useragent,
        '--disable-dev-shm-usage',
        
]

for obj in arguments: #Load every launch argument
     options.add_argument(obj)

if platform.system() == 'Windows':
    execpath = "././chromedriver.exe"
#macOS
elif platform.system() == 'Darwin':
    execpath = '/usr/local/bin/chromedriver'
##Linux
elif platform.system() == 'Linux':
    execpath = '/usr/bin/chromedriver'
##None Detected
else:
    raise exception('Insert Here!')
                

                
