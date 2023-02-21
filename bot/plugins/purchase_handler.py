from telegram import Update
from telegram.ext import CallbackContext

from bot import ADMIN_ID
from bot.database.db import BotUser, session


def purchase_callback_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = update.effective_user.id
    query_data = update.callback_query.data
    balance = 0
    with session:
        user = session.query(BotUser).filter(BotUser.user_id == user_id).first()
        if user:
            balance = user.balance

    if query_data == "purchase2000":
        if balance < 2000:
            return query.answer(text="You don't have enough balance", show_alert=True)

        if balance > 2000:
            query.answer(
                "Purchase Succesfull, Your request will be approved soon",
                show_alert=True,
            )
            context.bot.send_message(
                chat_id=ADMIN_ID,
                text=f"Card Purchased \nUser ID: {user_id}\nAmount: 2000\nTag: Visa without credit\n\nTo send card to this user use the command below\n\nExample:\n/card {user_id} 453410473171000737|12|2028|51010",
            )
            with session:
                user = session.query(BotUser).filter(BotUser.user_id == user_id).first()
                user.balance = user.balance - 2000
                session.commit()

    if query_data == "purchase3000":
        if balance < 3000:
            return query.answer(text="You don't have enough balance", show_alert=True)

        if balance > 3000:
            query.answer(
                "Purchase Succesfull, Your request will be approved soon",
                show_alert=True,
            )
            context.bot.send_message(
                chat_id=ADMIN_ID,
                text=f"Card Purchased \nUser ID: {user_id}\nAmount: 3000\nTag: Visa with 5$\n\nTo send card to this user use the command below\n\nExample:\n/card {user_id} 453410473171000737|12|2028|51010",
            )
            with session:
                user = session.query(BotUser).filter(BotUser.user_id == user_id).first()
                user.balance = user.balance - 3000
                session.commit()

    if query_data == "purchase6000":
        if balance < 6000:
            return query.answer(text="You don't have enough balance", show_alert=True)

        if balance > 6000:
            query.answer(
                "Purchase Succesfull, Your request will be approved soon",
                show_alert=True,
            )
            context.bot.send_message(
                chat_id=ADMIN_ID,
                text=f"Card Purchased \nUser ID: {user_id}\nAmount: 6000\nTag: Visa with 15$\n\nTo send card to this user use the command below\n\nExample:\n/card {user_id} 4534647317600737|12|2028|566",
            )
            with session:
                user = session.query(BotUser).filter(BotUser.user_id == user_id).first()
                user.balance = user.balance - 6000
                session.commit()

    if query_data == "purchase10000":
        if balance < 10000:
            return query.answer(text="You don't have enough balance", show_alert=True)

        if balance > 10000:
            query.answer(
                "Purchase Succesfull, Your request will be approved soon",
                show_alert=True,
            )
            context.bot.send_message(
                chat_id=ADMIN_ID,
                text=f"Card Purchased \nUser ID: {user_id}\nAmount: 10000\nTag: Visa with 50$\n\nTo send card to this user use the command below\n\nExample:\n/card {user_id} 453410473171000737|12|2028|51010",
            )
            with session:
                user = session.query(BotUser).filter(BotUser.user_id == user_id).first()
                user.balance = user.balance - 10000
                session.commit()

    if query_data == "purchase15000":
        if balance < 15000:
            return query.answer(text="You don't have enough balance", show_alert=True)

        if balance > 15000:
            query.answer(
                "Purchase Succesfull, Your request will be approved soon",
                show_alert=True,
            )
            context.bot.send_message(
                chat_id=ADMIN_ID,
                text=f"Card Purchased \nUser ID: {user_id}\nAmount: 15000\nTag: Visa with 100$\n\nTo send card to this user use the command below\n\nExample:\n/card {user_id} 453415473171500737|12|2028|51515",
            )
            with session:
                user = session.query(BotUser).filter(BotUser.user_id == user_id).first()
                user.balance = user.balance - 15000
                session.commit()
