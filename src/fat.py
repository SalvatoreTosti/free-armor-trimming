#Command line interface for clickLogger and clickPlayer classes.
from clickLogger import ClickLogger
from clickPlayer import ClickPlayer
import argparse

parser = argparse.ArgumentParser(description='Command line interface for clickLogger and clickPlayer')
parser.add_argument("log")
parser.add_argument("play")
parser.add_argument("filename")

args = parser.parse_args()
print args

loggingActive = False
playbackActive = False
filename = ""
if args.log == "t":
    loggingActive = True
elif args.play == "t":
    playbackActive = True
else:
    loggingActive = True
    playbackActive = (not loggingActive)

#logger = ClickLogger("test.txt")
logger = ClickLogger(args.filename)
player = ClickPlayer(args.filename)
