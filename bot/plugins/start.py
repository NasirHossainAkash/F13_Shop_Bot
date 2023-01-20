from telegram import Update ,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import CallbackContext


def start_handler(update:Update,context:CallbackContext):
    with open("assets/images/photo1.jpg", "rb") as photo:
        update.message.reply_photo(
        caption="""🏠 MAIN MENU

    Buy card 💳 - pay for the card using cryptocurrency, bank card

    Help 💬 - ask the operator a question

    Top up card 💸 – add money to the card

    Learn more 🤔 - find out information about the project

    My Cards 💰 - view a list of my active cards

    Referral - Refer and get Discount""",
            photo=photo,reply_markup=InlineKeyboardMarkup( 
                [ 
                    [InlineKeyboardButton("Buy Card 💳",callback_data="buy_card"),InlineKeyboardButton("Top Up Card 💵",callback_data="top_up_card")],
                    [InlineKeyboardButton("Help 💬",callback_data="help"),InlineKeyboardButton("Learn More 🌐",url="https://vcards.flashsd.net")],
                    [InlineKeyboardButton("My Cards 💰",callback_data="my_cards"),InlineKeyboardButton("Balance ✨",callback_data="balance")],
                    [InlineKeyboardButton("Referral 💌",callback_data="referral")]
                ]
            )   )
    