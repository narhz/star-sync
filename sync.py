import os
from time import sleep

from git import Repo

import devconfig


def sync():
    if os.path.exists(devconfig.LINUX_PATH):
        repo = Repo(devconfig.LINUX_PATH)

    if os.path.exists(devconfig.PHONE_PATH):
        repo = Repo(devconfig.PHONE_PATH)

    origin = repo.remotes.origin

    try:
        origin.pull()
    except Exception as e:
        print(e)

    try:
        repo.git.add('-A')
        repo.git.commit('-m', 'updated')
        origin.push()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    sync()
