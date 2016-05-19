#Command line interface for clickLogger and clickPlayer classes.
from clickLogger import ClickLogger
from clickPlayer import ClickPlayer
from keyLogger import KeyLogger
from keyPlayer import KeyPlayer
from eventEditor import EventEditor

import argparse
import os

class MODE:
    EXIT, ASK, EDIT, RECORD_CLICK, PLAY_CLICK, RECORD_KEY, PLAY_KEY = range(1,8)

class EDITOR_MODE:
    EDITOR_EXIT, EDITOR_ASK, EDITOR_LIST, EDITOR_MOVE, EDITOR_CHANGE_TIME = range(1,6)

class FAT(object):
    def __init__(self):
        pass

    def main(self):
        print "Free Armor Trimming v0.1 by Salvatore Tosti"
        running = True
        mode = MODE.ASK
        while running:
            if( mode == MODE.EXIT ):
                running = False #stop looping
            if( mode == MODE.ASK ):
                mode = self.promptForCommand()
            elif( mode == MODE.EDIT ):
                self.launchEventEditor()
                mode = MODE.ASK
            elif( mode == MODE.RECORD_CLICK ):
                self.launchClickLogger()
                mode = MODE.ASK
            elif( mode == MODE.PLAY_CLICK ):
                self.launchClickPlayer()
                mode = MODE.ASK
            elif( mode == MODE.RECORD_KEY ):
                self.launchKeyLogger()
                mode = MODE.ASK
            elif( mode == MODE.PLAY_KEY ):
                self.launchKeyPlayer()
                mode = MODE.ASK
            else:
                return


    def promptForCommand(self):
        userInput = raw_input("Enter an execution mode: ").lower()
        if( userInput == "exit" ):
            return MODE.EXIT
        elif( userInput == "edit" ):
            return MODE.EDIT
        elif( userInput == "record click" ):
            return MODE.RECORD_CLICK
        elif( userInput == "play click" ):
            return MODE.PLAY_CLICK
        elif( userInput == "record key" ):
            return MODE.RECORD_KEY
        elif( userInput == "play key" ):
            return MODE.PLAY_KEY
        else:
            return MODE.ASK

    def promptForFile(self):
        userInput = raw_input("Enter a file name: ")
        return userInput

    def launchClickLogger(self):
        filename = self.promptForFile()
        self._initClickLogger(filename)

    def _initClickLogger(self, args):
        clickLogger = ClickLogger(args)
        clickLogger.run()

    def launchClickPlayer(self):
        filename = self.promptForFile()
        self._initClickPlayer(filename)

    def _initClickPlayer(self, args):
        clickPlayer = ClickPlayer(args)
        clickPlayer.play()

    def launchKeyLogger(self):
        filename = self.promptForFile()
        keyLogger = KeyLogger(filename)
        keyLogger.run()

    def launchKeyPlayer(self):
        filename = self.promptForFile()
        keyPlayer = KeyPlayer(filename)
        keyPlayer.play()

    def launchEventEditor(self):
        filename = self.promptForFile()
        self._initEventEditor(filename)

    def _initEventEditor(self, args):
        eventEditor = EventEditor(args)
        editing = True
        editorMode = EDITOR_MODE.EDITOR_ASK

        while( editing ):
            if( editorMode == EDITOR_MODE.EDITOR_EXIT ):
                editing = False #leave editor mode loop
            elif( editorMode == EDITOR_MODE.EDITOR_ASK ):
                editorMode = self.promptForEditorCommand()
                pass
            elif( editorMode == EDITOR_MODE.EDITOR_LIST ):
                eventEditor.printNumberedEventList()
                editorMode = EDITOR_MODE.EDITOR_ASK
                pass
            elif( editorMode == EDITOR_MODE.EDITOR_MOVE ):
                oldPosition = self.promptForNumber()
                pass
            elif( editorMode == EDITOR_MODE.EDITOR_CHANGE_TIME ):
                pass
            else:
                return

    def promptForEditorCommand(self):
        userInput = raw_input("Enter an editor mode: ").lower()
        if( userInput == "exit" ):
            return EDITOR_MODE.EDITOR_EXIT
        elif( userInput == "list" ):
            return EDITOR_MODE.EDITOR_LIST
        elif( userInput == "move" ):
            return EDITOR_MODE.EDITOR_MOVE
        elif( userInput == "change time" ):
            return EDITOR_MODE.EDITOR_CHANGE_TIME
        else:
            return EDITOR_MODE.EDITOR_ASK

    def promptForOldPosition(self):
        userInput = raw_input("Enter a Number: ").lower()
        return userInput


if __name__ == '__main__':
    FAT().main()
