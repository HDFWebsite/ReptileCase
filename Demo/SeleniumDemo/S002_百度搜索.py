import time
from selenium import webdriver
driver = webdriver.Chrome('C:\\Users\\Administrator\\Downloads\\chromedriver.exe')
driver.get('https://www.baidu.com')
time.sleep(2)
# 输入python
kw_element = driver.find_element_by_id('kw')
kw_element.send_keys('python')

time.sleep(2)
# 点击 百度一下
su_element = driver.find_element_by_id('su')
su_element.click()

# input(222)
# element.send_keys()
# element.click()

"""常用的属性和方法"""
# driver.save_screenshot() 截图
# driver.title # 当前标签页的标题文本内容
print(driver.current_url) # 当前的url
print('='*10)
print(driver.page_source) # 网页的源代码(加载完毕或加载中的)
print('='*10)
print(driver.get_cookies()) # 当前标签页的cookies list

driver.quit()

