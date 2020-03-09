from  scrapy import Item, Field
from scrapy.loader.processors import MapCompose,TakeFirst



# the tag and headline is extracted from the title it has the format below 
# ‘Society still expects women to do all the caring’ | Books | The Guardian
# the first is the headline and the second is the tag
def parse_tag(text):
    return text.split('|')[1].strip()


def parse_head(text):
    return text.split('|')[0].strip()


class Article(Item):
    
    article  =  Field()
    authors  =  Field()
    headline =  Field(input_processor=MapCompose(parse_head),output_processor=TakeFirst())
    date     =  Field(input_processor=MapCompose(int),output_processor=TakeFirst())
    tag      =  Field(input_processor=MapCompose(parse_tag),output_processor=TakeFirst())
    url      =  Field(output_processor=TakeFirst())