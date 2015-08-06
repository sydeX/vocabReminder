import logging
from pymongo import MongoClient


logging.getLogger().setLevel(20)


class DBClient:
    def __init__(self, url=None, db_name='vocabReminder'):
        self.client = MongoClient(url)
        self.db_name = db_name
        self.db = self.client[db_name]

    def drop_db(self, db_name):
        self.client.drop_database(db_name)

        logging.info("Dropped DB %s" % db_name)

    def write(self, collection_name, key, content):
        collection = self.db[collection_name]

        if collection.find(key).count() > 0:
            raise('{key} already exist in {collection}!'.format(key=key, collection=collection))

        result = collection.insert_one(content)
        logging.info('Added {key} into {collection}. ID: {id}'.format(key=key,
                                                                      collection=collection,
                                                                      id=result.inserted_id))
