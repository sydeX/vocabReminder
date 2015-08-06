from db_utils import DBClient
from config import DB_NAME


class DBObject:
    def __init__(self, key_dict=None, db_name=DB_NAME, collection_name=None):
        self.key_dict = None
        self.db_name = db_name
        self.collection_name = collection_name

    def repr_json(self):
        return self.__dict__

    def write(self):
        client = DBClient(db_name=self.db_name)
        client.write(collection_name=self.collection_name, key=self.key_dict, content=self.repr_json())