from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from bot.database.db import BotUser, session


def balance_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    name = update.effective_user.first_name
    user_id = update.effective_user.id

    balance = 0
    with session:
        user = session.query(BotUser).filter(BotUser.user_id == user_id).first()
        if user:
            balance = user.balance

    # balance = get_balance(user_id)[0]
    query.edit_message_caption(
        f"<b>🪴 Balance</b> \n<b>Your Name:</b> {name}\n<b>User ID:</b> {user_id}\n<b>Balance: {balance} </b>",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Top Up", callback_data="top_up_card"),
                ],
                [InlineKeyboardButton(text="Home", callback_data="home")],
            ]
        ),
    )
