import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

from telegram import ParseMode
from telegram.ext import Defaults, Updater


ADMIN_ID = int(os.getenv("ADMIN_ID"))
if not ADMIN_ID:
    ADMIN_ID = 1301921132


TOKEN = os.getenv("TOKEN")
if not TOKEN:
    TOKEN = "5472393791:AAFTwZUtvv0vt70-rINcVUp1SGMzCESSN3o"
if not TOKEN:
    raise Exception("Token Not found on environment var")
defaults = Defaults(parse_mode=ParseMode.HTML, run_async=True)
updater = Updater(token=TOKEN, defaults=defaults)
dispatcher = updater.dispatcher
job_queue = updater.job_queue
