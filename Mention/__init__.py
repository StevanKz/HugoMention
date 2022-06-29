# Credits: @StevanKz
# Copyright (C) 2022 HugoMention
#
# This file is a part of < https://github.com/StevanKz/HugoMention/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/StevanKz/HugoMention/blob/main/LICENSE/>.
#
# t.me/StvnsYu & t.me/HugoSupport


import time
import asyncio
import logging

from logging.handlers import RotatingFileHandler
from pyromod import listen
from pyrogram import Client

from config import API_ID, API_HASH, BOT_TOKEN, WORKERS


app = Client(
    "Hugo-Mention",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=WORKERS,
    plugins={"root": "Mention.plugins"},
)


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("HugoMention.txt", maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

logs = logging.getLogger(__name__)
    
loop = asyncio.get_event_loop()

StartTime = time.time()
