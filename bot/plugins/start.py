import pickle

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from bot.database.db import BotUser, session


def start_handler(update: Update, context: CallbackContext):
    with session:
        bot_user = (
            session.query(BotUser)
            .filter(BotUser.user_id == update.effective_user.id)
            .first()
        )
        if not bot_user:
            session.add(
                BotUser(
                    user_id=update.effective_user.id,
                    balance=0,
                    first_name=update.effective_user.first_name,
                )
            )
            session.commit()

    with open("assets/images/photo1.jpg", "rb") as photo:
        update.message.reply_photo(
            caption="""🏠 MAIN MENU

    Buy card 💳 - pay for the card using cryptocurrency, bank card

    Help 💬 - ask the operator a question

    Top up card 💸 – add money to the card

    Learn more 🤔 - find out information about the project

    My Cards 💰 - view a list of my active cards

    Referral - Refer and get Discount""",
            photo=photo,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Buy Card 💳", callback_data="buy_card"),
                        InlineKeyboardButton(
                            "Top Up Card 💵", callback_data="top_up_card"
                        ),
                    ],
                    [
                        InlineKeyboardButton("Help 💬", callback_data="help"),
                        InlineKeyboardButton(
                            "Learn More 🌐", url="https://vcard.flashsd.net/"
                        ),
                    ],
                    [
                        InlineKeyboardButton("My Cards 💰", callback_data="my_cards"),
                        InlineKeyboardButton("Balance ✨", callback_data="balance"),
                    ],
                    [InlineKeyboardButton("Referral 💌", callback_data="referral")],
                ]
            ),
        )


def start_callback_handler(update: Update, context: CallbackContext):
    update.callback_query.answer()

    with open("assets/images/photo1.jpg", "rb") as photo:
        update.callback_query.edit_message_caption(
            caption="""🏠 MAIN MENU

    Buy card 💳 - pay for the card using cryptocurrency, bank card

    Help 💬 - ask the operator a question

    Top up card 💸 – add money to the card

    Learn more 🤔 - find out information about the project

    My Cards 💰 - view a list of my active cards

    Referral - Refer and get Discount""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Buy Card 💳", callback_data="buy_card"),
                        InlineKeyboardButton(
                            "Top Up Card 💵", callback_data="top_up_card"
                        ),
                    ],
                    [
                        InlineKeyboardButton("Help 💬", callback_data="help"),
                        InlineKeyboardButton(
                            "Learn More 🌐", url="https://vcard.flashsd.net/"
                        ),
                    ],
                    [
                        InlineKeyboardButton("My Cards 💰", callback_data="my_cards"),
                        InlineKeyboardButton("Balance ✨", callback_data="balance"),
                    ],
                    [InlineKeyboardButton("Referral 💌", callback_data="referral")],
                ]
            ),
        )
