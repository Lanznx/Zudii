# Action Chains

from turtle import update
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

path = "/Users/lanz/Downloads/檔案/chromedriver" ## webdriver 的路徑
driver = webdriver.Chrome(path)
driver.get("https://tsj.tw/") ## 遊戲網站


blow = driver.find_element(By.ID, "click") ## 開始吹
# blow_count = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[2]/h4[2]')

point = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[2]/h4[2]')
item = []
item.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[5]/button[1]'))
item.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[5]/button[1]/i'))
item.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[5]/button[1]'))

price = []
price.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[4]'))
price.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[4]'))
price.append(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[4]'))



actions = ActionChains(driver)

for u in range(1000): ## 一直吹
    money = int(point.text.replace("您目前擁有 ", "").replace("技術點", ""))
    print("m: ",money)
    actions.double_click(blow)
    actions.click(blow)
    actions.perform()
    for i in range(3):
        p = int(price[i].text.replace(" 技術點",""))
        print("p: ",p)

        if money >= p:
            update_blow = ActionChains(driver)
            update_blow.move_to_element(item[i])
            update_blow.click()
            update_blow.perform()
            break






