# -*- coding: utf-8 -*-
import scrapy


class Tencent1Spider(scrapy.Spider):
    name = 'tencent1'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        tr_list = (response.xpath('//table[@class="tablelist"]//tr'))
        for i in tr_list[1:-1]:
            item = {}
            item['title'] = i.xpath('.//a/text()').extract_first()
            yield item
        next_data = tr_list[-1].xpath('.//a[text()="下一页"]/@href').extract_first()
        if next_data != 'javascript:;':
            next_url = 'https://hr.tencent.com/' + next_data
            yield scrapy.Request(next_url, callback=self.parse)

