from telegram import Update,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import CallbackContext


def balance_handler(update:Update,context:CallbackContext):
    query = update.callback_query
    name = update.effective_user.first_name
    user_id = update.effective_user.id 

    # balance = get_balance(user_id)[0]
    query.edit_message_caption(f"<b>🪴 Balance</b> \n<b>Your Name:</b> {name}\n<b>User ID:</b> {user_id}\n<b>Balance: 0.00 </b>",reply_markup=InlineKeyboardMarkup( [ [
        InlineKeyboardButton("Top Up",callback_data="top_up_card"),
        
    ],
    [InlineKeyboardButton(text="Home",callback_data="home")]]))



