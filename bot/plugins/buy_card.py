from telegram import Update,InputMediaPhoto,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import CallbackContext
from bot.database.db import session,BotUser

def buy_card_cb_handler(update:Update,context:CallbackContext):
    cb = update.callback_query
    cb.answer()
    cb.edit_message_media(media=InputMediaPhoto(open("assets/images/photo2.jpg","rb"),caption="♠️ Please Select the Product you want to Purchase"),reply_markup=InlineKeyboardMarkup(
            
            [   [InlineKeyboardButton("Card Visa without USD", callback_data="visa")],
                [InlineKeyboardButton("Card Visa with 5 USD", callback_data="visa5")],
                [InlineKeyboardButton("Card Visa with 15 USD", callback_data="visa15")],
                [InlineKeyboardButton("Card Visa with 50 USD", callback_data="visa50")],
                [
                    InlineKeyboardButton(
                        "Card Visa with 100 USD", callback_data="visa100"
                    )
                ],
                [InlineKeyboardButton("Home",callback_data="home")]
            ]
        ),
    )

def visa_callback_handler(update:Update,context:CallbackContext):
    query = update.callback_query
    user_id = update.effective_user.id 
    balance = 0
    with session:
        user = session.query(BotUser).filter(BotUser.user_id == user_id).first()
        if user:
            balance = user.balance
        if not user:
            session.add(BotUser(user_id=user_id,first_name=update.effective_user.first_name,balance=0))
            session.commit()


    if query.data == "visa5":
        query.edit_message_caption(
            f"💳 Visa Card \n💵 Preloaded Balance: 5$ USD\n\n✳️ Price: 3000 rub\n\nYour Balance: {balance}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Click here to purchase", callback_data="purchase3000"
                        )
                    ],
                                        [
                        InlineKeyboardButton(
                            "Back", callback_data="buy_card"
                        )
                    ]
                ]
            ),
        )

    if query.data == "visa15":
        query.edit_message_caption(
            f"💳 Visa Card \n💵 Preloaded Balance: 15$ USD\n\n✳️ Price:  6000 rub\n\nYour Balance: {balance}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Click here to purchase", callback_data="purchase6000"
                        )
                    ],
                                        [
                        InlineKeyboardButton(
                            "Back", callback_data="buy_card"
                        )
                    ]
                ]
            ),
        )

    if query.data == "visa50":
        query.edit_message_caption(
           f"💳Visa Card \n💵 Preloaded Balance: 50$ USD\n\n✳️ Price: 10000 ru\n\nYour Balance: {balance}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Click here to purchase", callback_data="purchase10000"
                        )
                    ],
                                        [
                        InlineKeyboardButton(
                            "Back", callback_data="buy_card"
                        )
                    ]
                ]
            ),
        )

    if query.data == "visa100":
        query.edit_message_caption(
            f"💳 Visa Card \n💵 Preloaded Balance: 100$ USD\n\n✳️ Price: 15000 rub\n\nYour Balance: {balance}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Click here to purchase", callback_data="purchase15000"
                        )
                    ],
                                        [
                        InlineKeyboardButton(
                            "Back", callback_data="buy_card"
                        )
                    ]
                ]
            ),
        )
    if query.data == "visa":
        query.edit_message_caption(
            f"💳 Visa Card \n💵 Preloaded Balance: 0$ USD\n\n✳️ Price: 2000 rub\n\nYour Balance: {balance}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Click here to purchase", callback_data="purchase2000"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "Back", callback_data="buy_card"
                        )
                    ]
                ]
            ),
        )




def purchase_query_handler(update:Update,context:CallbackContext):
    cb = update.callback_query
    cb.answer()
    