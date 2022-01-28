## 爬取 FB
## 帳號：109305033@g.nccu.edu.tw
## 密碼：Zudii@Andiidii

from email.headerregistry import Group
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import requests
from datetime import datetime
# import sqlite3 # fot sqlute database support
from bs4 import BeautifulSoup


## -------- 路徑、帳密要自己改 --------
path = "/Users/lanz/Downloads/檔案/chromedriver"
driver = webdriver.Chrome(path)
driver.get("https://zh-tw.facebook.com/")
user = driver.find_element_by_id("email")
user.send_keys("109305033@g.nccu.edu.tw")
password = driver.find_element_by_id("pass")
password.send_keys("Zudii@Andiidii")
## -------- 路徑、帳密要自己改 --------
log_in = driver.find_element_by_name("login")
log_in.click()

## 關通知
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_setting_values':{'notifications': 2}}
options.add_experimental_option('prefs', prefs)

## 前往政大租客
time.sleep(2)
driver.get('https://www.facebook.com/groups/NCCU.zuker')
























