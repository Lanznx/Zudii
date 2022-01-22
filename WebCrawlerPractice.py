# selenium tutorial
# https://www.youtube.com/watch?v=ximjGyZ93YQ&t=1867s

from pydoc import classname
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = "/Users/lanz/Downloads/檔案/chromedriver"
driver = webdriver.Chrome(path)

driver.get("https://www.dcard.tw/f") ## 前往Ｄ卡
print(driver.title)
search = driver.find_element_by_name("query")
search.send_keys("政大企管")
search.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "pkcmwm-1"))
)
titles = driver.find_elements_by_class_name("tgn9uw-3") ## get title of the website

for title in titles:
    print(title.text)

time.sleep(5)
driver.quit() ## close the chrome


