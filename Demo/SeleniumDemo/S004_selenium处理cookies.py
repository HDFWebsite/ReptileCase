from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\Administrator\\Downloads\\chromedriver.exe')

driver.get('https://www.baidu.com')

cookies_list = driver.get_cookies() # 全部cookies list

# 转换为字典
cookies_dict = {cookie['name']:cookie['value'] for cookie in cookies_list}
print(cookies_list)
print(cookies_dict)

# 删除一个cookie
cookie_name = input('输入一个要删除的cookie的name:')
driver.delete_cookie(cookie_name)

print(driver.get_cookies())

# 删除全部cookies
driver.delete_all_cookies()

print(driver.get_cookies())

driver.quit()