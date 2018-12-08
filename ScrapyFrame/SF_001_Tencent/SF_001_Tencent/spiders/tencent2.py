# -*- coding: utf-8 -*-
import scrapy
from SF_001_Tencent.items import Sf001TencentItem

class Tencent2Spider(scrapy.Spider):
    name = 'tencent2'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        tr_list = (response.xpath('//table[@class="tablelist"]//tr'))
        for i in tr_list[1:-1]:
            title = i.xpath('.//a/text()').extract_first()
            detail_url = 'https://hr.tencent.com/' + i.xpath('.//a/@href').extract_first()
            yield scrapy.Request(detail_url,
                                 callback=self.parse_detail,
                                 meta={"title": title}
                                 )

        next_data = tr_list[-1].xpath('.//a[text()="下一页"]/@href').extract_first()
        if next_data != 'javascript:;':
            next_url = 'https://hr.tencent.com/' + next_data
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_detail(self, response):
        item = Sf001TencentItem()
        item['title'] = response.meta['title']
        item['content'] = response.xpath('//ul[@class="squareli"]/li/text()').extract()
        yield item
