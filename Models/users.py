from config import USERS_COLLECTION_NAME
from db_object import DBObject
from Models.flashcards import Flashcard


class User(DBObject):

    def __init__(self, email,
                 first_name,
                 last_name,
                 db_name='vocabReminder',
                 key_dict=None,
                 collection_name=USERS_COLLECTION_NAME,
                 flashcard_id_list=[],
                 _id=None):

        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.flashcard_id_list = flashcard_id_list
        self.key_dict = key_dict or {'email': self.email}
        self.db_name = db_name
        self.collection_name = collection_name
        self.id = _id

    def add_flashcard(self, cue, value):
        card = Flashcard(cue, value, self._id)
        card_id = card.write_or_update()
        self.flashcard_id_list.append(card_id)
        self.write_or_update()
