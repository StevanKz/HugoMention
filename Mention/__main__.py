# Credits: @StevanKz
# Copyright (C) 2022 HugoMention
#
# This file is a part of < https://github.com/StevanKz/HugoMention/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/StevanKz/HugoMention/blob/main/LICENSE/>.
#
# t.me/StvnsYu & t.me/HugoSupport


from pyrogram import idle
from uvloop import install

from Mention.misc import git, heroku
from Mention import app, logs, loop


async def start_bot():
    try:
        await app.start()
    except Exception as a:
        logs.warning(a)
    await idle()


if __name__ == "__main__":
    logs.info("Starting Mention-Bot")
    install()
    git()
    heroku()
    logs.info("Hugo Mention Started Successfully !")
    loop.run_until_complete(start_bot())
