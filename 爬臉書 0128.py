from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from email.headerregistry import Group
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from sqlalchemy import null

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

for i in range(5):
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)

# u=0
# clicks_more = chrome.find_elements_by_name('顯示更多')
# while(clicks_more != null):
#     clicks_more[u].click()
#     u += 1


soup = BeautifulSoup(chrome.page_source, 'html.parser')
## 找出所有內文
contents = soup.find_all('div', {'class': 'ecm0bbzt hv4rvrfc ihqw7lf3 dati1w0a'})

line = 0
for content in contents: 
    ## 把內文的每一行都找出來，並印出來
    posts = content.find_all('div', {'dir': 'auto'}, {'style': "text-align: start"})
    for post in posts:
        print(post.getText())   
    print("-----------")

