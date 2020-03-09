from  scrapy import Item, Field
from scrapy.loader.processors import MapCompose,TakeFirst



def parse_tag(text):
    return text.split('|')[-2].strip()


class Article(Item):
    
    article  =  Field()
    authors  =  Field()
    headline =  Field(input_processor=MapCompose(str.strip),output_processor=TakeFirst())
    date     =  Field(input_processor=MapCompose(int),output_processor=TakeFirst())
    tag      =  Field(input_processor=MapCompose(parse_tag),output_processor=TakeFirst())
    url      =  Field(output_processor=TakeFirst())