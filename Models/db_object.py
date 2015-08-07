from db_utils import DBClient
from config import DB_NAME


class DBObject(object):
    def __init__(self, key_dict=None, db_name=DB_NAME, collection_name=None):
        self.key_dict = key_dict
        self.db_name = db_name
        self.collection_name = collection_name
        self.id = None

    def repr_json(self):
        return self.__dict__

    def write_or_update(self):
        client = DBClient(db_name=self.db_name)
        inserted_id = client.write_or_update(collection_name=self.collection_name, key=self.key_dict, content=self.repr_json())
        self.id = inserted_id or self.id
        return self.id
