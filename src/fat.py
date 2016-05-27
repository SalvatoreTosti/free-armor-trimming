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
    EDITOR_EXIT, EDITOR_ASK, EDITOR_LIST, EDITOR_MOVE, EDITOR_CHANGE_TIME, EDITOR_CHANGE_EVENT, EDITOR_SAVE = range(1,8)

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
                mode = self._promptForCommand()
            elif( mode == MODE.EDIT ):
                self._launchEventEditor()
                mode = MODE.ASK
            elif( mode == MODE.RECORD_CLICK ):
                self._launchClickLogger()
                mode = MODE.ASK
            elif( mode == MODE.PLAY_CLICK ):
                self._launchClickPlayer()
                mode = MODE.ASK
            elif( mode == MODE.RECORD_KEY ):
                self._launchKeyLogger()
                mode = MODE.ASK
            elif( mode == MODE.PLAY_KEY ):
                self._launchKeyPlayer()
                mode = MODE.ASK
            else:
                return


    def _promptForCommand(self):
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

    def _promptForFile(self):
        userInput = raw_input("Enter a file name: ")
        return userInput

    def _launchClickLogger(self):
        filename = self._promptForFile()
        clickLogger = ClickLogger(filename)
        clickLogger.run()

    def _launchClickPlayer(self):
        filename = self._promptForFile()
        clickPlayer = ClickPlayer(filename)
        clickPlayer.play()

    def _launchKeyLogger(self):
        filename = self._promptForFile()
        keyLogger = KeyLogger(filename)
        keyLogger.run()

    def _launchKeyPlayer(self):
        filename = self._promptForFile()
        keyPlayer = KeyPlayer(filename)
        keyPlayer.play()

    def _launchEventEditor(self):
        while True:
            userInput = self._promptForFile()
            if(os.path.isfile(userInput)):
                self._runEventEditor(userInput)
                return
            elif(userInput == "exit"):
                return

    def _runEventEditor(self, args):
        eventEditor = EventEditor(args)
        editing = True
        editorMode = EDITOR_MODE.EDITOR_ASK

        while( editing ):
            if( editorMode == EDITOR_MODE.EDITOR_EXIT ):
                editing = False #leave editor mode loop
            elif( editorMode == EDITOR_MODE.EDITOR_ASK ):
                editorMode = self._promptForEditorCommand()
            elif( editorMode == EDITOR_MODE.EDITOR_LIST ):
                eventEditor.printNumberedEventList()
                editorMode = EDITOR_MODE.EDITOR_ASK
            elif( editorMode == EDITOR_MODE.EDITOR_MOVE ):
                oldPosition = self._promptForNumber()
                newPosition = self._promptForNumber()
                eventEditor._moveEvent(int(oldPosition),int(newPosition))
                editorMode = EDITOR_MODE.EDITOR_ASK
            elif( editorMode == EDITOR_MODE.EDITOR_CHANGE_TIME ):
                self._editorChangeTimeHelper(eventEditor)
                editorMode = EDITOR_MODE.EDITOR_ASK
                pass
            elif( editorMode == EDITOR_MODE.EDITOR_CHANGE_EVENT ):
                pass
            elif( editorMode == EDITOR_MODE.EDITOR_SAVE):
                self._editorSaveHelpers(eventEditor)
                editorMode = EDITOR_MODE.EDITOR_ASK
            else:
                return

    def _promptForEditorCommand(self):
        userInput = raw_input("Enter an editor mode: ").lower()
        if( userInput == "exit" ):
            return EDITOR_MODE.EDITOR_EXIT
        elif( userInput == "list" ):
            return EDITOR_MODE.EDITOR_LIST
        elif( userInput == "move" ):
            return EDITOR_MODE.EDITOR_MOVE
        elif( userInput == "change time" ):
            return EDITOR_MODE.EDITOR_CHANGE_TIME
        elif( userInput == "change event"):
            return EDITOR_MODE.EDITOR_CHANGE_Event
        elif( userInput == "save" ):
            return EDITOR_MODE.EDITOR_SAVE
        else:
            return EDITOR_MODE.EDITOR_ASK

    def _editorSaveHelpers(self, eventEditor):
            if(not eventEditor.eventsInOrder()):
                reorder = self._promptYN("Events are not ordered chronologically, reorder events? (Y/N)")
                if(reorder):
                    eventEditor.sortListByTime()
            try:
                eventEdtior.writeEventList(eventEditor.readLocaion)
            except IOError:
                print "Unable to open file"

    def _editorChangeTimeHelper(self,eventEditor):
        editPosition = self._promptForNumber()
        event = None
        try:
            event = eventEditor.getEvent(int(editPosition))
        except IndexError:
            print "Number outside of valid range."
            return
        except ValueError:
            print "Invalid input, please enter a number."
            return
            
        newTime = self._promptForNumber()
        try:
            newEvent = eventEditor._changeEventTime(float(newTime),event)
        except ValueError:
            print "Invalid input, please enter a number."
            return
        eventEditor.setEvent(int(editPosition),newEvent)

    def _promptForNumber(self):
        userInput = raw_input("Enter a Number: ").lower()
        return userInput

    def _promptYN(self, prompt):
        while True:
            userInput = raw_input(prompt).lower()
            if(userInput == 'y' or userInput == 'yes'):
                return True
            elif(userInput == 'n' or userInput == 'no'):
                return False
            else:
                pass #do nothing continue looping

if __name__ == '__main__':
    FAT().main()
