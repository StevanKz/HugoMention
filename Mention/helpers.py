import asyncio
import heroku3
import shlex
# Credits: @StevanKz
# Copyright (C) 2022 HugoMention
#
# This file is a part of < https://github.com/StevanKz/HugoMention/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/StevanKz/HugoMention/blob/main/LICENSE/>.
#
# t.me/StvnsYu & t.me/HugoSupport


import socket
from typing import Tuple 

from config import Config
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError


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
    str(Config.HEROKU_API_KEY),
    "https",
    str(Config.HEROKU_APP_NAME),
    "HEAD",
    "main",
]


class Helpers(object):
    def install_req(self, cmd: str) -> Tuple[str, str, int, int]:
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

    def git(self):
        REPO_LINK = self.REPO_URL
        if self.GIT_TOKEN:
            GIT_USERNAME = REPO_LINK.split("com/")[1].split("/")[0]
            TEMP_REPO = REPO_LINK.split("https://")[1]
            UPSTREAM_REPO = f"https://{GIT_USERNAME}:{self.GIT_TOKEN}@{TEMP_REPO}"
        else:
            UPSTREAM_REPO = self.REPO_URL
        try:
            repo = Repo()
            self.logs.info(f"Git Client Found")
        except GitCommandError:
            self.logs.info(f"Invalid Git Command")
        except InvalidGitRepositoryError:
            repo = Repo.init()
            if "origin" in repo.remotes:
                origin = repo.remote("origin")
            else:
                origin = repo.create_remote("origin", UPSTREAM_REPO)
            origin.fetch()
            repo.create_head(
                self.BRANCH,
                origin.refs[self.BRANCH],
            )
            repo.heads[self.BRANCH].set_tracking_branch(origin.refs[self.BRANCH])
            repo.heads[self.BRANCH].checkout(True)
            try:
                repo.create_remote("origin", self.REPO_URL)
            except BaseException:
                pass
            nrs = repo.remote("origin")
            nrs.fetch(self.BRANCH)
            try:
                nrs.pull(self.BRANCH)
            except GitCommandError:
                repo.git.reset("--hard", "FETCH_HEAD")
            self.install_req("pip3 install --no-cache-dir -U -r requirements.txt")
            self.logs.info("Fetched Latest Updates")

    def is_heroku(self):
        return "heroku" in socket.getfqdn()

    def heroku(self):
        global HAPP
        if self.is_heroku:
            if self.HEROKU_API_KEY and self.HEROKU_APP_NAME:
                try:
                    Heroku = heroku3.from_key(self.HEROKU_API_KEY)
                    HAPP = Heroku.app(self.HEROKU_APP_NAME)
                    self.logs.info(f"Heroku App Configured")
                except BaseException as e:
                    self.logs.error(e)
                    self.logs.info(
                        f"Make sure your HEROKU_API_KEY and HEROKU_APP_NAME are properly configured in heroku config vars."
                    )
