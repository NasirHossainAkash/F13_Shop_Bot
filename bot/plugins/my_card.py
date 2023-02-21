from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from bot.database.db import Cards, session


def my_card_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = update.effective_user.id
    cards_string = ""
    with session:
        cards = session.query(Cards).filter(Cards.user_id == user_id).all()
        if cards:
            for card in cards:
                cards_string += f"{card.cards}\n"

    if not cards_string:
        cards_string = "No active cards available"

    query.edit_message_caption(
        caption=f"""👤 Your Active Cards\n
    
{cards_string}
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Home", callback_data="home")]]
        ),
    )
