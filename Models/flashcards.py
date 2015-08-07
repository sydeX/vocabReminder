from reminders import Reminder
from db_object import DBObject
from config import FLASHCARDS_COLLECTION_NAME


class Flashcard(DBObject):

    def __init__(self, cue,
                 value,
                 user_id,
                 db_name='vocabReminder',
                 key_dict=None,
                 collection_name=FLASHCARDS_COLLECTION_NAME,
                 reminder=None,
                 _id=None):

        self.id = _id
        self.cue = cue
        self.value = value
        self.user_id = user_id
        self.db_name = db_name
        self.collection_name = collection_name
        self.reminder = reminder
        self.key_dict = key_dict or {'cue': cue, 'value': value}

    def set_reminder(self, interval, incremental_interval):
        reminder = Reminder(self.id,
                            self.user_id,
                            interval=interval,
                            incremental_interval=incremental_interval)

        reminder_id = reminder.write_or_update()
        self.reminder = reminder_id
        self.write_or_update()
