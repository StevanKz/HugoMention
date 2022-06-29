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

from Mention import app


async def start_bot():
    try:
        await app.start()
    except Exception as a:
        app.logs.warning(a)
    await idle()


if __name__ == "__main__":
    app.logs.info("Starting Hugo Mention")
    install()
    app.git()
    app.heroku()
    app.logs.info("Hugo Mention Started Successfully !")
    app.loop.run_until_complete(start_bot())
