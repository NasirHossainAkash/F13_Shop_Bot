from telegram import Update,InputMediaPhoto,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import CallbackContext


def buy_card_cb_handler(update:Update,context:CallbackContext):
    cb = update.callback_query
    cb.answer()
    cb.edit_message_media(media=InputMediaPhoto(open("assets\images\photo2.jpg","rb"),caption="♠️ Please Select the Product you want to Purchase"),reply_markup=InlineKeyboardMarkup(
            
            [   [InlineKeyboardButton("Card Visa without USD", callback_data="visa")],
                [InlineKeyboardButton("Card Visa with 5 USD", callback_data="visa5")],
                [InlineKeyboardButton("Card Visa with 15 USD", callback_data="visa15")],
                [InlineKeyboardButton("Card Visa with 50 USD", callback_data="visa50")],
                [
                    InlineKeyboardButton(
                        "Card Visa with 100 USD", callback_data="visa100"
                    )
                ],
            ]
        ),
    )

def visa_callback_handler(update:Update,context:CallbackContext):
    query = update.callback_query

    if query.data == "visa5":
        query.edit_message_caption(
            "💳 Visa Card \n💵 Preloaded Balance: 5$ USD\n\n✳️ Price: 3000 rub\n\nYour Balance: 0.00",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Click here to purchase", callback_data="purchase3000"
                        )
                    ]
                ]
            ),
        )

    if query.data == "visa15":
        query.edit_message_caption(
            "💳 Visa Card \n💵 Preloaded Balance: 15$ USD\n\n✳️ Price:  6000 rub\n\nYour Balance: 0.00",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Click here to purchase", callback_data="purchase6000"
                        )
                    ]
                ]
            ),
        )

    if query.data == "visa50":
        query.edit_message_caption(
            "💳Visa Card \n💵 Preloaded Balance: 50$ USD\n\n✳️ Price: 10000 ru\n\nYour Balance: 0.00",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Click here to purchase", callback_data="purchase10000"
                        )
                    ]
                ]
            ),
        )

    if query.data == "visa100":
        query.edit_message_caption(
            "💳 Visa Card \n💵 Preloaded Balance: 100$ USD\n\n✳️ Price: 15000 rub\n\nYour Balance: 0.00",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Click here to purchase", callback_data="purchase15000"
                        )
                    ]
                ]
            ),
        )
    if query.data == "visa":
        query.edit_message_caption(
            "💳 Visa Card \n💵 Preloaded Balance: 0$ USD\n\n✳️ Price: 2000 rub\n\nYour Balance: 0.00",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Click here to purchase", callback_data="purchase2000"
                        )
                    ]
                ]
            ),
        )




def purchase_query_handler(update:Update,context:CallbackContext):
    cb = update.callback_query
    cb.answer()
    