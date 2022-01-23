# Action Chains

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

path = "/Users/lanz/Downloads/檔案/chromedriver" ## webdriver 的路徑
driver = webdriver.Chrome(path)
driver.get("https://tsj.tw/") ## 遊戲網站


blow = driver.find_element(By.ID, "click") ## 開始吹
# blow_count = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[2]/h4[2]')

actions = ActionChains(driver)
for u in range(1000): ## 一直吹
    actions.click(blow)
    actions.double_click(blow)
    actions.perform()
    




