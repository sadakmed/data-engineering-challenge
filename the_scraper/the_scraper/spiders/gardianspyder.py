import scrapy
from bs4 import BeautifulSoup as soup

roo="https://www.theguardian.com"
depth=1
global count
count=0
nmbArticles=3
class GardianSpyder(scrapy.Spider):
	name = "GardianSpyder"
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
		print('\nparsing pagination :\t', response.url,f'parsed {len(articles)} articles')

		for article in articles:
			yield scrapy.Request(url=article,callback=self.parse_article)

		next_pagination=response.css('div.pagination__list a::attr(href)').getall()

		if next_pagination is not None:
#			print('this is the next pagination pages',next_pagination)
			if '=' in next_pagination[-1] and int(next_pagination[-1].split('=')[-1]) < 4:
				print('\nthis is where we\'re going:',next_pagination[-1])

				yield response.follow(next_pagination[-1],callback=self.parse_pagination)


	def parse_article(self,response):
		if self.isArticle(response):
			text=soup("\n".join(response.css('div.content__article-body > p').getall()),'html.parser' ).text
			headline=response.css('div > h1.content__headline::text').get()     
			print('\nparsing article : ', response.url)
			authors=response.css('p.byline span span::text').getall()  
			if authors is None:
				authors=response.css('div.meta__contact-wrap p.byline::text').getall()  

			date=response.css('p.content__dateline > time::attr(data-timestamp)').get() 
			tag=response.css('title::text').get().split('|')[-2].strip()
			yield {
				'article':text,
				'headline':headline,
				'authors':authors,
				'date':date,
				'tag':tag,
				'url': response.url
			}


		elif self.isPagination(response):
			self.parse_pagination(response)
		else:
			return

		

	def isArticle(self,response):
		return response.css('div.content__article-body > p')


	def isPagination(self,response):
		return response.css('div.pagination__list a::attr(href)')
	

			  


