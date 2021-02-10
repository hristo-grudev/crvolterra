import re

import scrapy

from scrapy.loader import ItemLoader
from ..items import CrvolterraItem
from itemloaders.processors import TakeFirst


class CrvolterraSpider(scrapy.Spider):
	name = 'crvolterra'
	start_urls = ['https://www.crvolterra.it/media/archivio-news/']

	def parse(self, response):
		post_links = response.xpath('//article[@class="column-equal col-md-12 "]/h3/a/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

	def parse_post(self, response):
		title = response.xpath('//div[@class="title-header"]/h2//text()').get()
		description = response.xpath('//div[@class="entry-content"]//text()[normalize-space()]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//div[@class="newsdate"]/text()').get()

		item = ItemLoader(item=CrvolterraItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
