import pymongo
from the_scraper import settings






class SavePipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(settings.MONGODB_HOST)
        self.collection=client.get_database()[settings.MONGODB_COLLECTION]



    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
