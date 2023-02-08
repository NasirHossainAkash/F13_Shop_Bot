from telegram import Update,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import CallbackContext


def my_card_handler(update:Update,context:CallbackContext):
    query = update.callback_query


    # cards = get from database 
    query.edit_message_caption(caption="""👤 Your Active Cards\n
    
4535908451022453|04|2028|286
4535907187410248|08|2026|578
4535904407610525|05|2026|135
""",reply_markup=InlineKeyboardMarkup([ [ 
        InlineKeyboardButton(text="Home",callback_data="home")
]]))