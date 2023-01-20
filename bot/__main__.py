import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)



from telegram.ext import CommandHandler,Filters,MessageHandler

from bot import dispatcher,job_queue,updater
from bot.plugins.start import start_handler


def main():
    dispatcher.add_handler(CommandHandler("start",start_handler))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()