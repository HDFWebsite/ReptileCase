# -*- coding: utf-8 -*-
import scrapy


class Login1Spider(scrapy.Spider):
    name = 'login1'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/HDFWebsite']  # 这个起始的url需要登陆后/携带cookie才能获取

    def start_requests(self):
        """构造request,携带cookie,并返回"""
        cookies_str = '_octo=GH1.1.1086654774.1532419215; _ga=GA1.2.101469216.1532419214; user_session=c-elEAIJ7DJ-DuGHpXeP6kBNDpr8bQkznS7-JSsXOphnxyjD; __Host-user_session_same_site=c-elEAIJ7DJ-DuGHpXeP6kBNDpr8bQkznS7-JSsXOphnxyjD; logged_in=yes; dotcom_user=HDFWebsite; has_recent_activity=1; tz=Asia%2FShanghai; _gh_sess=MlI4bVpWVVcxRjB4S3FpY2d6czBWYy9aYnp0N0s3Q215K1JJaEF3eVFBa1JhclJhZjI2L0ZnTnFzNHh1UlJ0clF0Mlk1SEZ4RG4zanhOdjRvM3Axd3ZTeHBWL3AzSnc0SzlNb0ZvTldjc1VJV0dRc2xkbzVzSSs4TnYvd3h2NFlqajcyTGtYWitPV1cwdlM0bGdaNHlFN0RhRzRJaUxaTSt0eXhYcFRnS1MraXpCNkpjSHdJcUtyL0NtRUxaZmx5RU1YWHY5dzBac1FLeFE3aFIrUzZ2Zz09LS1sak9YRGVUNVd1eEFzZkQ4MEFZUkd3PT0%3D--875a9351d4ac702d9f504f3198979c15697d349a'
        cookies_dict = {cookie.split('=')[0]: cookie.split('=')[1]
                        for cookie in cookies_str.split('; ')}
        print(cookies_dict)
        yield scrapy.Request(self.start_urls[0],
                             cookies=cookies_dict,
                             callback=self.parse)

    def parse(self, response):
        with open('login1.html', 'w',encoding='utf-8') as f:
            f.write(response.body.decode())

