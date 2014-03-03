import os
import random 
import subprocess

DEVNULL = open(os.devnull, 'w')


def play_misc(fileName):

        baseDir = os.path.dirname(os.path.realpath(__file__)) + "/sounds/misc"
        audio = baseDir + "/" +fileName
        subprocess.call(["mplayer",audio],stdout=DEVNULL, stderr=subprocess.STDOUT)


def play_from_dir(folderName):

    baseDir = os.path.dirname(os.path.realpath(__file__)) + "/sounds/" + folderName
    audio = baseDir + "/" + random.choice(os.listdir(baseDir))
    subprocess.call(["mplayer",audio,"&>/dev/null"], stdout=DEVNULL, stderr=subprocess.STDOUT)
