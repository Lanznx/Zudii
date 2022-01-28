from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from email.headerregistry import Group
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--disable-notifications")

## -------- 路徑、帳密要自己改 --------
chrome = webdriver.Chrome('/Users/lanz/Downloads/檔案/chromedriver')
chrome.get("https://www.facebook.com/")

email = chrome.find_element_by_id("email")
password = chrome.find_element_by_id("pass")

email.send_keys('109305033@g.nccu.edu.tw')
password.send_keys('Zudii@Andiidii')
password.submit()
## -------- 路徑、帳密要自己改 --------

time.sleep(3)
chrome.get('https://www.facebook.com/groups/NCCU.zuker')

# clicks_more = chrome.find_elements_by_css_selector('.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gpro0wi8.oo9gr5id.lrazzd5p')

for i in range(5):
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)


soup = BeautifulSoup(chrome.page_source, 'html.parser')
## 找出所有內文
contents = soup.find_all('div', {'class': 'kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q'})

for content in contents:
    ## 把內文的每一行都找出來，並印出來
    posts = content.find_all('div', {'dir': 'auto'}, {'style': "text-align: start"})
    
    for post in posts:
        if post:
            print(post.getText()) 
    
    print("-----------")
