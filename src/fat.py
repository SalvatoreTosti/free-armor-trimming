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
        group = parser.add_mutually_exclusive_group(required = True)
        group.add_argument("--log", type=str, help="activate mouse click logging mode.")
        group.add_argument("--edit", type=str, help="edit mouse click file.")
        group.add_argument("--play", type=str, help="active mouse click playback mode.")
        args = parser.parse_args()

        if args.log:
            self.initClickLogger(args.log)
        elif args.play:
            if not os.path.isfile(str(os.getcwd()+ "/"+args.play)):
                print "Invalid file selected."
                return
            else:
                self.initClickPlayer(args.play)
        elif args.edit:
            if not os.path.isfile(str(os.getcwd()+ "/"+args.play)):
                print "Invalid file selected."
                return
            else:
                print "edit mode"

    def initClickLogger(self, args):
        clickLogger = ClickLogger(args)
        clickLogger.run()

    def initClickPlayer(self, args):
        clickPlayer = ClickPlayer(args)
        clickPlayer.printCoordinateList()

if __name__ == '__main__':
    FAT().main()
