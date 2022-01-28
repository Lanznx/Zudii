from pydoc import cli
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from sympy import content


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

for x in range(1, 4):
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
soup = BeautifulSoup(chrome.page_source, 'html.parser')
## 找出所有內文
contents = soup.find_all('div', {'class': 'kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q'})

# click_more = chrome.find_element_by_css_selector('.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gpro0wi8.oo9gr5id.lrazzd5p')

for content in contents:
    ## 把內文的每一行都找出來，並印出來
    posts = content.find_all('div', {'dir': 'auto'}, {'style': "text-align: start"})

    for post in posts:
        if post:
            print(post.getText()) 
    # click_more.click()
    print("-----------")
