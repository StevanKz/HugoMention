# Credits: @StevanKz
# Copyright (C) 2022 HugoMention
#
# This file is a part of < https://github.com/StevanKz/HugoMention/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/StevanKz/HugoMention/blob/main/LICENSE/>.
#
# t.me/StvnsYu & t.me/HugoSupport


import asyncio
import logging

from logging.handlers import RotatingFileHandler

from config import Config
from .helpers import Helpers


class Utils(Config, Helpers):
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
        handlers=[
            RotatingFileHandler("MentionBot.txt", maxBytes=50000000, backupCount=10),
            logging.StreamHandler(),
        ],
    )
    logging.getLogger("pyrogram").setLevel(logging.WARNING)

    logs = logging.getLogger(__name__)
    
    loop = asyncio.get_event_loop()
