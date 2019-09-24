import os
from time import sleep

from git import Repo

import devconfig


def sync():
    if os.path.exists(devconfig.LINUX_PATH):
        repo = Repo(devconfig.LINUX_PATH)
        origin = repo.remotes.origin

        origin.pull()

        repo.git.add('-A')
        repo.git.commit('-m', 'updated')
        origin.push()


    if print(os.path.exists(devconfig.PHONE_PATH)):
        repo = Repo(devconfig.PHONE_PATH)

        origin = repo.remotes.origin

        origin.pull()

        repo.git.add('-A')
        repo.git.commit('-m', 'updated')
        origin.push()


if __name__ == '__main__':
    sync()
