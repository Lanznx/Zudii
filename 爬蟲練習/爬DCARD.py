# selenium tutorial
# https://www.youtube.com/watch?v=ximjGyZ93YQ&t=1867s
# 練習用 Selenium 來操作 Dcard

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = "/Users/lanz/Downloads/檔案/chromedriver" ## webdriver 的路徑
driver = webdriver.Chrome(path)

driver.get("https://www.dcard.tw/f") ## 前往Ｄ卡
search = driver.find_element_by_name("query")
search.clear()
search.send_keys("比特幣") ## 輸入“比特幣”
search.send_keys(Keys.RETURN) ## 傳送資料
# search.clear()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "sc-3yr054-1"))
) ## Wait for the page loading

titles = driver.find_elements_by_class_name("tgn9uw-3") ## get title of the website

for title in titles:
    print(title.text)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME,"sc-1s9033j-0"))
) ## Wait for the page loading

link = driver.find_element_by_class_name("bJQtxM")
link.click()
time.sleep(2)
driver.back()

time.sleep(2)
driver.quit() ## close the chrome








































































































































































































































































































































