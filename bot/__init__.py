import os 

import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

from telegram import ParseMode
from telegram.ext import Defaults,Updater


TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise("Token Not found on environment var")
defaults = Defaults(parse_mode=ParseMode.HTML,run_async=True)
updater = Updater(token=TOKEN,defaults=defaults)
dispatcher = updater.dispatcher
job_queue = updater.job_queue