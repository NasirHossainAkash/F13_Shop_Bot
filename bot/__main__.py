import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)



from telegram.ext import CommandHandler,Filters,MessageHandler,CallbackQueryHandler

from bot import dispatcher,job_queue,updater
from bot.plugins.start import start_handler,start_callback_handler
from bot.plugins.buy_card import buy_card_cb_handler,visa_callback_handler
from bot.plugins.balance import balance_handler
def main():
    dispatcher.add_handler(CommandHandler("start",start_handler))
    dispatcher.add_handler(CallbackQueryHandler(callback=buy_card_cb_handler,pattern="buy_card"))
    dispatcher.add_handler(CallbackQueryHandler(callback=visa_callback_handler,pattern="visa"))
    dispatcher.add_handler(CallbackQueryHandler(callback=balance_handler,pattern="balance"))
    dispatcher.add_handler(CallbackQueryHandler(callback=start_callback_handler,pattern='home'))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()