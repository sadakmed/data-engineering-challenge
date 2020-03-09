from scrapy import Spider, Request
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup as soup
from the_scraper.items import Article

roo="https://www.theguardian.com"
depth=1
nmbArticles=3


class GardianSpyder(Spider):
	name = "GardianSpyder"
	allowed_domains = ['theguardian.com']
	start_urls = ["https://www.theguardian.com/uk"]

	def parse(self, response):    
		urls = response.css('#main-menu > div > ul.menu-group.menu-group--primary a::attr(href)').getall()		
		for url in urls:
			yield response.follow(url,callback=self.parse_second_page)

	def parse_second_page(self,response):
	
		if self.isPagination(response):
			self.parse_pagination(response)

		to_all=response.css('a.treats__treat::attr(href)').get()
		if to_all:
			a="".join((roo,to_all))
			yield response.follow(url=a, callback=self.parse_pagination)


	def parse_pagination(self,response):
		articles=response.css('div > section a::attr(href)').getall()
		#print('\nparsing pagination :\t', response.url,f'parsed {len(articles)} articles')

		for article in articles:
			yield Request(url=article,callback=self.parse_article)

		next_pagination=response.css('div.pagination__list a::attr(href)').getall()

		if next_pagination is not None:
			if '=' in next_pagination[-1] and int(next_pagination[-1].split('=')[-1]) < depth+1:
				# print('\nthis is where we\'re going:',next_pagination[-1])

				yield response.follow(next_pagination[-1],callback=self.parse_pagination)


	def parse_article(self,response):
		if self.isArticle(response):

			loader=ItemLoader(item=Article() , selector=response)
			
			article=list(map(lambda x : soup(x,'html.parser').text ,response.css('div.content__article-body > p').getall())	)
			
			authors=response.css('p.byline span span::text').getall()  
			if len(authors) == 0 :
				authors=response.css('div.meta__contact-wrap p.byline::text').getall()  
			if len(authors) == 0:
				authors=['unkown']
			
			loader.add_value('authors',authors)
			loader.add_value('article',article)
			loader.add_value('url',response.url)

			loader.add_css('headline','title::text')
			loader.add_css('tag','title::text')
			loader.add_css('date','p.content__dateline > time::attr(data-timestamp)')


			yield loader.load_item()


		elif self.isPagination(response):
			self.parse_pagination(response)
		else:
			return

		

	def isArticle(self,response):
		return response.css('div.content__article-body > p')


	def isPagination(self,response):
		return response.css('div.pagination__list a::attr(href)')
	

			  


