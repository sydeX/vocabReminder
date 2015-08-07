from Models.users import User
from Models.flashcards import Flashcard
from Models.reminders import Reminder
from datetime import date, timedelta
from db_utils import DBClient, json_decoder
from config import DB_NAME, FLASHCARDS_COLLECTION_NAME, REMINDERS_COLLECTION_NAME

def main():
    # Initiailze DB
    client = DBClient()
    client.drop_db(DB_NAME)

    # Create an user account
    user = User('xineyang@gmail.com', 'Elaine', 'Yang')
    user_id = user.write_or_update()

    # Create a new flashcards
    user.add_flashcard(cue='Intrigue', value='arouse the curiosity or interest of; fascinate.')

    # Find a flashcard from user account
    cards = client.find(collection_name=FLASHCARDS_COLLECTION_NAME, key={'_id': {'$in': user.flashcard_id_list}})

    # Set up a reminder for the first flashcard. The reminder will be sent out every 2 days until a cancelling logic has been triggered
    # Or if incremental_interval is True, the interval will get doubled at the each time
    card = json_decoder(Flashcard, cards[0])
    card.set_reminder(2, True)

    # Print out all the reminders for today for this user
    today = date.today() + timedelta(days=2)
    r = client.find(collection_name=REMINDERS_COLLECTION_NAME, key={'user_id': user_id, 'next_reminder_datestr': str(today)})
    r = json_decoder(Reminder, r[0])

    assert(card.id == r.card_id)

if __name__ == '__main__':
    main()