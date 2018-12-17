import requests
import json
import js2py

# - 实现思路:
#   - 使用session发送rKey获取登录需要信息
#     - url: http://activity.renren.com/livecell/rKey
#     - 方法: get
#  获取session对象
session = requests.session()
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Type":"application/x-www-form-urlencoded"
}
# 设置session的请求头信息
session.headers = headers

#获取上边js执行过程中用到的三个Js文件中的js代码
url = 'http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/RSA.js'
resp = session.get(url)
with open('./js/RSA.js', 'w') as f:
    f.write(resp.text)
url = 'http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/BigInt.js'
resp = session.get(url)
with open('./js/BigInt.js', 'w') as f:
    f.write(resp.text)
url = 'http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/Barrett.js'
resp = session.get(url)
with open('./js/Barrett.js', 'w') as f:
    f.write(resp.text)