from config import REMINDERS_COLLECTION_NAME
from db_object import DBObject
from datetime import date, timedelta
from dateutil.parser import parse

class Reminder(DBObject):

    def __init__(self, card_id,
                 user_id,
                 last_reminder_datestr=None,
                 next_reminder_datestr=None,
                 interval=1,
                 incremental_interval=False,
                 db_name='vocabReminder',
                 key_dict=None,
                 collection_name=REMINDERS_COLLECTION_NAME,
                 _id=None):

        self.id = _id
        self.card_id = card_id
        self.user_id = user_id
        self.interval = interval
        self.last_reminder_datestr = last_reminder_datestr or str(date.today())
        self.next_reminder_datestr = next_reminder_datestr or str(self._convert_str_to_date(self.last_reminder_datestr) + timedelta(days=interval))
        self.incremental_interval = incremental_interval
        self.key_dict = key_dict or {'cardId': self.card_id}
        self.db_name = db_name
        self.collection_name = collection_name

    def _convert_str_to_date(self, date):
        if isinstance(date, str):
            return parse(date).date()
        else:
            return date

    def update_reminder(self):
        self.last_reminder_datestr = date.today()
        self.next_reminder_datestr = self.last_reminder_datestr + timedelta(days=self.interval)

        self.last_reminder_datestr = self._convert_str_to_date(self.last_reminder_datestr)
        self.next_reminder_datestr = self._convert_str_to_date(self.next_reminder_datestr)

        if self.incremental_interval:
            self.interval += self.interval

        self.write_or_update()
