from config import USERS_COLLECTION
from db_object import DBObject


class User(DBObject):

    def __init__(self, email, first_name, last_name, db_name='vocabReminder'):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.db_name = db_name
        self.flashcards = None

        super(User).__init__(key_dict={'email': self.email}, db_name=db_name, collection_name=USERS_COLLECTION)