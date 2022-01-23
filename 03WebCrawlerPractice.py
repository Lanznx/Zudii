## 爬取 IG
## 帳號：Zudii_an
## 密碼：Zudii@Andiidii

import time 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



path = "/Users/lanz/Downloads/檔案/chromedriver"
driver = webdriver.Chrome(path)
driver.get("https://www.instagram.com/")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)

user = driver.find_element_by_name("username")
user.send_keys("Zudii_an")
password = driver.find_element_by_name("password")
password.send_keys("Zudii@Andiidii")
logIn = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
logIn.click()


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
)

search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search.send_keys("shiba")
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)







