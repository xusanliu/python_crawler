# -*- coding: utf-8 -*-
import scrapy


class LaughSpider(scrapy.Spider):
	name = 'laugh'
	allowed_domains = ['xiaohua.zol.com']
	start_urls = [
		"http://xiaohua.zol.com.cn/lengxiaohua/1.html",
		"http://xiaohua.zol.com.cn/lengxiaohua/2.html"
	]

	def parse(self, response):
		page=response.url.split('/')[-1][0]
		file_name='laugh_{}.txt'.format(page)
		with open(file_name,'w') as f:
			laughs=response.css('.artcle-summary')
			for laugh in laughs:
				title=laugh.css('.article-title::text').extract()[0]
				content=laugh.css('.summary-text::text').extract()[0]
				print('title:/n',title)
				print('content:/n',content)
				f.write('title:{}/n content:{}/n',format(title,content))

