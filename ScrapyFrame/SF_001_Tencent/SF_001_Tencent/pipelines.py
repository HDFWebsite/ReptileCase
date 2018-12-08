# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

def write_data(name,item):
    file_path = 'SF_001_Tencent\\TextData\\'+name+'.txt'
    with open(file_path, 'a',encoding='utf-8') as  file:
        data = ''
        for key ,value in item.items():
            if key =='content':
                now_data = '\n{}:[{}]\n'.format(key," ".join(value))
            else:
                now_data = '{}:{}'.format(key, value)
            data += now_data
        file.write(data + '\n')

class Sf001TencentPipeline(object):
    def process_item(self, item, spider):
        write_data(spider.name,item)
        return item
