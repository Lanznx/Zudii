# 爬 IG 練習
# 自動追一堆妹子

from re import I
import time 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from sqlalchemy import null

path = "/Users/lanz/Downloads/檔案/chromedriver"
driver = webdriver.Chrome(path)
driver.get("https://www.instagram.com/")



WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
## 輸入帳號密碼並登入
name = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")

name.send_keys("Zudii_an")
password.send_keys("Zudii@Andiidii")

log_in = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
log_in.click()


## 按稍等一下，並進入 IG 頁面
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button'))
)
later01 = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
later01.click()

## 因為這邊好像有不只一個稍等一下，所以我弄一個回圈把所有的 稍等一下 都按一遍
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.aOOlW.HoLwm'))
)
later02 = driver.find_elements_by_css_selector('.aOOlW.HoLwm')
for later in later02:
    later.click()

## 點進去許月的帳號
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.XTCLo.d_djL.DljaH'))
)
profile = driver.find_element_by_css_selector('.XTCLo.d_djL.DljaH')
profile.send_keys("yueh_0720")
time.sleep(2)
profile.send_keys(Keys.RETURN)
profile.send_keys(Keys.RETURN)


## 按下倒三角的「更多」來看更多 ig 帳號
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '._5f5mN.-fzfL.KUBKM.yZn4P'))
)
profile_more = driver.find_element_by_css_selector('._5f5mN.-fzfL.KUBKM.yZn4P')
profile_more.click()

## 可以開始追蹤了！
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".sqdOP.L3NKy._4pI4F.y3zKF"))
)
follows = driver.find_elements_by_css_selector(".sqdOP.L3NKy._4pI4F.y3zKF") ## 找出所有可以追蹤的按鍵


rights = driver.find_element_by_css_selector(".Kf8kP.coreSpritePagingChevron") ## 找出往右的鍵

WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.CSS_SELECTOR, ".sqdOP.L3NKy._4pI4F.y3zKF"))
)

i = 0
for follow in follows:
    follow.click()
    rights[i].click()
    i += 1










