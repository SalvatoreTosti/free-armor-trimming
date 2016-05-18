#Command line interface for clickLogger and clickPlayer classes.
from clickLogger import ClickLogger
from clickPlayer import ClickPlayer

import argparse
import os

class MODE:
    EXIT,ASK,EDIT,RECORD_CLICK,PLAY_CLICK,RECORD_MOUSE,PLAY_MOUSE = range(1,8)

class FAT(object):
    def __init__(self):
        pass

    def main(self):
        print "Free Armor Trimming v0.1 by Salvatore Tosti"
        running = True
        mode = MODE.ASK
        while running:
            if(mode == MODE.EXIT):
                running = False #stop looping
            if(mode == MODE.ASK):
                mode = self.promptForCommand()
            elif(mode == MODE.EDIT):
                pass #not implemented yet
            elif(mode == MODE.RECORD_CLICK):
                self.launchClickLogger()
                mode = MODE.ASK
                pass
            elif(mode == MODE.RECORD_MOUSE):
                pass
            elif(mode == MODE.PLAY_MOUSE):
                pass
            else:
                return


    def promptForCommand(self):
        print ""
        userInput = raw_input("Enter an execution mode: ").lower()
        if(userInput == "exit"):
            return MODE.EXIT
        elif(userInput == "edit"):
            return MODE.EDIT
        elif(userInput == "record click"):
            return MODE.RECORD_CLICK
        elif(userInput == "play click"):
            return MODE.PLAY_CLICK
        elif(userInput == "record key"):
            return MODE.RECORD_CLICK
        elif(userInput == "play click"):
            return MODE.PLAY_CLICK
        else:
            return MODE.ASK

    def promptForFile(self):
        userInput = raw_input("Enter a file name: ")
        return userInput

    def launchClickLogger(self):
        filename = self.promptForFile()
        self.initClickLogger(filename)

    def initClickLogger(self, args):
        clickLogger = ClickLogger(args)
        clickLogger.run()

    def initClickPlayer(self, args):
        clickPlayer = ClickPlayer(args)
        clickPlayer.printCoordinateList()

if __name__ == '__main__':
    FAT().main()
