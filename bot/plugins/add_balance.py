from telegram import Update
from telegram.ext import CallbackContext

from bot import ADMIN_ID
from bot.database.db import BotUser, session


def add_balance_handler(update: Update, context: CallbackContext):
    if not update.effective_user.id == ADMIN_ID:
        return update.message.reply_text("You are not authorized")

    try:
        user_id = int(context.args[0])
        amount = int(context.args[1])

    except IndexError:
        return update.message.reply_text("You have to provide user_id and amount.. ")

    except ValueError:
        return update.message.reply_text("Invalid User ID or Amount")

    with session:
        user = session.query(BotUser).filter(BotUser.user_id == user_id).first()
        if not user:
            return update.message.reply_text("User not found on database")

        user.balance += amount
        session.commit()
        return update.message.reply_text(
            f"{amount} added to {user_id} aka {user.first_name} "
        )
