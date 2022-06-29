# Credits: @StevanKz
# Copyright (C) 2022 HugoMention
#
# This file is a part of < https://github.com/StevanKz/HugoMention/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/StevanKz/HugoMention/blob/main/LICENSE/>.
#
# t.me/StvnsYu & t.me/HugoSupport


import asyncio
import heroku3
import shlex
import socket
from typing import Tuple 

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError

from config import HEROKU_APP_NAME, HEROKU_API_KEY, GIT_TOKEN, REPO_URL, BRANCH
from Mention import logs

HAPP = None
XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(HEROKU_API_KEY),
    "https",
    str(HEROKU_APP_NAME),
    "HEAD",
    "main",
]


def install_req(cmd: str) -> Tuple[str, str, int, int]:
    async def install_requirements():
        args = shlex.split(cmd)
        process = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        return (
            stdout.decode("utf-8", "replace").strip(),
            stderr.decode("utf-8", "replace").strip(),
            process.returncode,
            process.pid,
        )

    return asyncio.get_event_loop().run_until_complete(install_requirements())

def git():
    REPO_LINK = REPO_URL
    if GIT_TOKEN:
        GIT_USERNAME = REPO_LINK.split("com/")[1].split("/")[0]
        TEMP_REPO = REPO_LINK.split("https://")[1]
        UPSTREAM_REPO = f"https://{GIT_USERNAME}:{GIT_TOKEN}@{TEMP_REPO}"
    else:
        UPSTREAM_REPO = REPO_URL
    try:
        repo = Repo()
        logs.info(f"Git Client Found")
    except GitCommandError:
        logs.info(f"Invalid Git Command")
    except InvalidGitRepositoryError:
        repo = Repo.init()
        if "origin" in repo.remotes:
            origin = repo.remote("origin")
        else:
            origin = repo.create_remote("origin", UPSTREAM_REPO)
        origin.fetch()
        repo.create_head(
            BRANCH,
            origin.refs[BRANCH],
        )
        repo.heads[BRANCH].set_tracking_branch(origin.refs[BRANCH])
        repo.heads[BRANCH].checkout(True)
        try:
            repo.create_remote("origin", REPO_URL)
        except BaseException:
            pass
        nrs = repo.remote("origin")
        nrs.fetch(BRANCH)
        try:
            nrs.pull(BRANCH)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        install_req("pip3 install --no-cache-dir -U -r requirements.txt")
        logs.info("Fetched Latest Updates")
        
        
def is_heroku():
    return "heroku" in socket.getfqdn()

    
def heroku():
    global HAPP
    if is_heroku:
        if HEROKU_API_KEY and HEROKU_APP_NAME:
            try:
                Heroku = heroku3.from_key(HEROKU_API_KEY)
                HAPP = Heroku.app(HEROKU_APP_NAME)
                logs.info(f"Heroku App Configured")
            except BaseException as e:
                logs.error(e)
                logs.info(
                    f"Make sure your HEROKU_API_KEY and HEROKU_APP_NAME are properly configured in heroku config vars."
                )