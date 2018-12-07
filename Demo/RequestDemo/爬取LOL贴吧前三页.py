import requests
i = 0
User_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
Cookie = 'BAIDUID=A5AD26D06BE914D9378B732DE2291CA1:FG=1; BIDUPSID=A5AD26D06BE914D9378B732DE2291CA1; PSTM=1527421056; TIEBA_USERTYPE=998a33cf5db48b1329c14405; bdshare_firstime=1527421149899; BDUSS=S1jVmY4WUVhQnNuaWx1NWpmM0pPNUo0RUJMNWdtYmlJZjdJVEp5ajN5Y09sOEJiQVFBQUFBJCQAAAAAAAAAAAEAAAAph9tqYmFiedXmt7MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA4KmVsOCplba; TIEBAUID=cd4907613b359cecb4ca5b07; STOKEN=839db2276387b8bcbbec93d9e1ad7c02546ad380d38d62aeea7c69ab5d936c62; Hm_lvt_287705c8d9e2073d13275b18dbd746dc=1540911968,1540991532; MCITY=-%3A; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[nxEBHQCyNxC]=WWrcCWdntFCTLn3rjb4rj63QhPEUf; H_PS_PSSID=; delPer=0; PSINO=1; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1540911964,1540991528,1542161449; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1542161449; 1792771881_FRSVideoUploadTip=1'

while i <3:
    url = 'https://tieba.baidu.com/f?kw=lol&ie=utf-8&pn={}'.format(i * 50)
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': Cookie,
        'Host': 'tieba.baidu.com',
        'Referer': 'https://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=%d' % (i + 1) * 50,
        'User-Agent': User_Agent
    }
    print(url)
    response = requests.get(url=url,headers=headers)
    with open('LOL/lol贴吧第%d页.txt'%(i+1),'w',encoding='utf-8') as f:
        f.write(response.text)
        print('第%d页写入完成'%(i+1))
        i +=1
