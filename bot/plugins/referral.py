from telegram import Update,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import CallbackContext


def referral_handler(update:Update,context:CallbackContext):
    query = update.callback_query
    query.answer()
    user_id = update.effective_user.id 
    refer_link = f"https://t.me/vkartybot?start={user_id}"
    query.edit_message_caption(f"""⭐️ Refer and Earn Extra\n\n♻️ Your Referral Link: \n<code>{refer_link}</code>""",reply_markup=InlineKeyboardMarkup( 
        [ 
        [InlineKeyboardButton("Home",callback_data="home")]
        ]
    ))