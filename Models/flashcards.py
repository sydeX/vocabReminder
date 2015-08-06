from datetime import date
from reminders import Reminder
from db_object import DBObject
from config import FLASHCARDS_COLLECTION


class Flashcard(DBObject):

    def __init__(self, cue, value, user_id, db_name='vocabReminder'):
        self.cue = cue
        self.value = value
        self.userId = user_id

        self.reminder = None

        super(Flashcard).__init__(key_dict={'cue': cue, 'value': value},
                                  db_name=db_name,
                                  collection_name=FLASHCARDS_COLLECTION)

    def set_reminder(self, interval, incremental):
        last_reminder_date = date(2015, 8, 5)
        next_reminder_date = date(2015, 8, 7)
        reminder = Reminder(self, self.userId, date.today(), last_reminder_date, next_reminder_date, next_reminder_date, interval, incremental)
        self.reminder = reminder
