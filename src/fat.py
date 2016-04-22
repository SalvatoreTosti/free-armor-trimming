#Command line interface for clickLogger and clickPlayer classes.
from clickLogger import ClickLogger
from clickPlayer import ClickPlayer

import argparse
import os

class FAT(object):
    def __init__(self):
        pass

    def main(self):
        parser = argparse.ArgumentParser(description='Command line interface for clickLogger and clickPlayer')
        parser.add_argument("--log", type=str, help="activate mouse click logging mode.")
        parser.add_argument("--play", type=str, help="active mouse click playback mode.")

        args = parser.parse_args()

        if args.log:
            logging = True
        else:
            logging = False

        if args.play:
            playback = True
        else:
            playback = False

        if logging and playback:
            print "Only one mode can be active at a time."
            return
        elif logging:
            self.initClickLogger(args.log)
        elif playback:
            if not os.path.isfile(str(os.getcwd()+ "/"+args.play)):
                print "Invalid file selected."
                return
            else:
                self.initClickPlayer(args.play)

    def initClickLogger(self, args):
        clickLogger = ClickLogger(args)
        clickLogger.run()

    def initClickPlayer(self, args):
        clickPlayer = ClickPlayer(args)
        clickPlayer.printCoordinateList()

if __name__ == '__main__':
    FAT().main()
