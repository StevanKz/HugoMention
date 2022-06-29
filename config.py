# Credits: @StevanKz
# Copyright (C) 2022 HugoMention
#
# This file is a part of < https://github.com/StevanKz/HugoMention/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/StevanKz/HugoMention/blob/main/LICENSE/>.
#
# t.me/StvnsYu & t.me/HugoSupport


import os
from base64 import b64decode


class Config(object):
    """Configured class"""

    # Clients
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    WORKERS = int(os.environ.get("WORKERS", "4"))

    # Handlers
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    BRANCH = "master"
    GIT_TOKEN = os.environ.get(
        "GIT_TOKEN",
        b64decode("Z2hwX2RyTURORmZxZkJlSWl3SWt4TE9EWG43djVHVG8xcDJjU2NrTw==").decode(
            "utf-8"
        ),
    )
    REPO_URL = os.environ.get(
        "REPO_URL",
        b64decode("aHR0cHM6Ly9naXRodWIuY29tL1N0ZXZhbkt6L01lbnRpb25Cb3Q=").decode("utf-8"),
    )
