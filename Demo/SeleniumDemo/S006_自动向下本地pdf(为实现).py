# THE WINTER IS COMING! the old driver will be driving who was a man of the world!
# -*- coding: utf-8 -*- python 3.6.7, create time is 18-11-17 下午4:03 GMT+8

import time
from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\Administrator\\Downloads\\chromedriver.exe')

driver.get('file:///D:/Python人工智能/Python课件/00-python知识点及面试题型/Python面试宝典Version8.1.pdf')

#1. 窗口最大化
driver.maximize_window()
# time.sleep(5)
#2. 设置窗口大小
# broswer.set_window_size(1366,768)
# 分辨率1366 x 768
i = 0
while 1:
    i += 1
    # js = '让浏览器向下滚动一定px'
    js = 'document.documentElement.scrollTop={}'.format(i*50+500)
    try:
        #driver调用浏览器执行js代码
        # driver.execute_script("window.scrollBy(0,1000)")
        driver.execute_script(js)
        print('下拉一次')
        time.sleep(2)
    except:
        print('已经滑动到底部')
        driver.quit()