# Credits: @StevanKz
# Copyright (C) 2022 HugoMention
#
# This file is a part of < https://github.com/StevanKz/HugoMention/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/StevanKz/HugoMention/blob/main/LICENSE/>.
#
# t.me/StvnsYu & t.me/HugoSupport


import sys

from pyromod import listen
from pyrogram import Client

from .utils import Utils


class HugoMention(Client, Utils):
    def __init__(self):
        super().__init__(
            "Hugo-Mention",
            api_id=self.API_ID,
            api_hash=self.API_HASH,
            bot_token=self.BOT_TOKEN,
            workers=self.WORKERS,
            plugins={"root": "Mention.plugins"},
        )

    async def start(self):
        await super().start()
        bot_me = await self.get_me()
        self.name = bot_me.first_name

    async def stop(self, *args):
        await super().stop()
        self.logs.info("Bot stopped.")


app = HugoMention()
