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

path = "/Users/lanz/Downloads/檔案/chromedriver"
driver = webdriver.Chrome(path)
driver.get("https://zh-tw.facebook.com/")

user = driver.find_element_by_id("email")
user.send_keys("109305033@g.nccu.edu.tw")
password = driver.find_element_by_id("pass")
password.send_keys("Zudii@Andiidii")
log_in = driver.find_element_by_name("login")
log_in.click()

## 等到政大租客跑出來之後就點下去
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="mount_0_0_Lt"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/div[2]/ul/li/div/a/div[1]/div[2]/div/div/div/div/span/span'))
)
group_nccu = driver.find_element_by_xpath('//*[@id="mount_0_0_Lt"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/div[2]/ul/li/div/a/div[1]/div[2]/div/div/div/div/span/span')
group_nccu.click()



## 展開所有的「顯示更多」
mores = driver.find_elements_by_class_name("oajrlxb2")
for more in mores:
    more.click()





















