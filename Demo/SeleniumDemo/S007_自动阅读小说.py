# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-17 下午4:03 GMT+8

import time
from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\Administrator\\Downloads\\chromedriver.exe')

driver.get('https://m.luocs.cn/11/11188/8327041_1.html')

#1. 窗口最大化
driver.maximize_window()

def xiala(i):
    time.sleep(2)
    # js = '让浏览器向下滚动一定px'
    js = 'document.documentElement.scrollTop={}'.format(i * 100)
    # driver调用浏览器执行js代码
    driver.execute_script(js)
    print('下拉一次')
i = 0
current_url = ''
while 1:
    try:
        su_element = driver.find_element_by_id('pb_next')
        while i <= 11:
            i+=1
            current_url= driver.current_url
            xiala(i)
        if su_element:
            i = 0
            time.sleep(2)
            su_element.click()
    except:
        print('浏览器已关闭,当前的url为：')
        print(current_url)
        driver.quit()
        break