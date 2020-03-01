'''
@Descripttion: 
@version: 
@Author: Bend Function
@Date: 2020-02-27 18:19:31
@LastEditors: Bend Function
@LastEditTime: 2020-02-27 22:03:39
'''
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

list = []
# 读比赛内容
with open("w2.txt","r",encoding='utf-8') as f:
    lines = f.readlines()
    # print(line)
    for line in lines:
        # 空行和换行符不计
        if line != '' and line != "\n":
            list.append(line)

# 使用Firefox
driver = webdriver.Firefox()
# 打开比赛网页
# A68X1
driver.get('https://dazi.kukuw.com/?tdsourcetag=s_pctim_aiomsg')
time.sleep(15)


for i in range(0,len(list)):
    # 如果单句太短就直接输出
    if len(list[i]) < 6:
        driver.switch_to.active_element.send_keys(list[i])
        time.sleep(0.2)
        continue
    
    # 每次输入 step 个字符
    startIndex = 0
    step = random.randint(3,7)
    endIndex = step
    while True:
        if endIndex < len(list[i]) - 2:
            driver.switch_to.active_element.send_keys(list[i][startIndex:endIndex])
        else:
            driver.switch_to.active_element.send_keys(list[i][startIndex:len(list[i]) - 2])
            break
        
        startIndex = endIndex
        endIndex += step
        time.sleep(0.2)
        
    time.sleep(0.3)
    back_num = random.randint(1,3)
    # 退3格,刷下退格数
    for k in range(0,back_num):
        driver.switch_to.active_element.send_keys(Keys.BACKSPACE)
    time.sleep(0.2)
    # 补完
    driver.switch_to.active_element.send_keys(list[i][len(list[i])-back_num-2:len(list[i])])
    time.sleep(0.4)
    # driver.switch_to.active_element.sendKeys(Keys.RETURN)
    # time.sleep(3.9)
