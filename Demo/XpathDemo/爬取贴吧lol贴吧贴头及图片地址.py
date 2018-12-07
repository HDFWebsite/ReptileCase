import requests
from lxml import etree

class TeiBaSpider(object):
    def __init__(self,spider_name,page=0):
        self.start_url = 'https://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw={}&lp=5011&lm=&pn=0'.format(
            spider_name)
        self.base_url = 'https://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
        }
        self.page = page
        self.ipage = 0
        self.text = 'TextData/tieba.txt'
    def _clear_text(self):
        with open(self.text,'w+') as f:
            f.truncate()
    def _save_title(self,item):
        with open(self.text,'a',encoding='utf-8') as f:
            f.write(item)
            f.write('\n')
    def _save_image(self,item):
        with open(self.text,'a',encoding='utf-8') as f:
            f.write(item)
            f.write('\n')

    def _get_detail_item(self,url):
        html = requests.get(url=url, headers=self.headers)
        html_element = etree.HTML(html.content)
        detail_url_title = html_element.xpath('/html/body/div/div[1]/strong')[0].text
        print(detail_url_title)
        self._save_title(detail_url_title)
        #图片url
        detail_url_image_list= html_element.xpath('/html/body/div/div[2]//img')
        for image_url in detail_url_image_list:
            self._save_image(image_url.xpath('@src')[0])

    def _handel_main(self,next_spider_url):
        self.ipage +=1
        html = requests.get(url=next_spider_url,headers=self.headers)
        html_element = etree.HTML(html.content)
        detail_url_list = html_element.xpath('//div[@class="i"or"i x"]/a')[1:21]
        for url in detail_url_list:
            url_to = self.base_url + url.xpath('@href')[0]
            self._get_detail_item(url_to)
        if html_element.xpath('//a[text()="下一页"]/@href') !=[] and self.ipage <self.page:
            next_spider_url = html_element.xpath('//a[text()="下一页"]/@href')
            next_all_spider_url = self.base_url+next_spider_url[0]
            print('下一页url'+next_all_spider_url)
            self._handel_main(next_all_spider_url)


    def run(self):
        self._clear_text()
        self._handel_main(self.start_url)

if __name__ == '__main__':

    spider = TeiBaSpider('lol',page=2)
    spider.run()