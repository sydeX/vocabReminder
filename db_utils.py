import logging
import json
from collections import namedtuple
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

    def write_or_update(self, collection_name, key, content):
        collection = self.db[collection_name]
        result_id = None

        if collection.find(key).count() > 0:
            logging.info('{key} already exist in {collection}!'.format(key=key, collection=collection))
            collection.update_one(key, {"$set": content, "$currentDate": {"lastModified": True}})
            logging.info('Updated {key} in {collection}.'.format(key=key, collection=collection))
        else:
            result_id = collection.insert_one(content).inserted_id
            logging.info('Added {key} into {collection}. ID: {id}'.format(key=key,
                                                                      collection=collection,
                                                                      id=result_id))

        return result_id

    def find(self, collection_name, key):
        collection = self.db[collection_name]
        return collection.find(key)

def json_decoder(cls, data):
    data.pop('id')
    return cls(**data)