from config import REMINDERS_COLLECTION
from db_object import DBObject


class Reminder(DBObject):

    def __init__(self, card_id,
                 user_id,
                 last_reminder_date,
                 next_reminder_date,
                 interval=1,
                 incremental=False,
                 db_name='vocabReminder'):

        self.cardId = card_id
        self.userId = user_id
        self.last_reminder_date = last_reminder_date
        self.next_reminder_date = next_reminder_date
        self.interval = interval
        self.incremental_interval = incremental

        super(Reminder, self).__init__(key_dict={'cardId': self.cardId},
                                       db_name=db_name,
                                       collection_name=REMINDERS_COLLECTION)

    def update_reminder(self):
        pass
