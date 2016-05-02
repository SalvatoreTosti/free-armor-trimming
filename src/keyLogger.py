from pykeyboard import PyKeyboardEvent

import time
import pickle

#OSX keys
key_code_translate_table = {
 0x00 : 'a',
 0x01 : 's',
 0x02 : 'd',
 0x03 : 'f',
 0x04 : 'h',
 0x05 : 'g',
 0x06 : 'z',
 0x07 : 'x',
 0x08 : 'c',
 0x09 : 'v',
 0x0b : 'b',
 0x0c : 'q',
 0x0d : 'w',
 0x0e : 'e',
 0x0f : 'r',
 0x10 : 'y',
 0x11 : 't',
 0x12 : '1',
 0x13 : '2',
 0x14 : '3',
 0x15 : '4',
 0x16 : '6',
 0x17 : '5',
 0x18 : '=',
 0x19 : '9',
 0x1a : '7',
 0x1b : '-',
 0x1c : '8',
 0x1d : '0',
 0x1e : ']',
 0x1f : 'o',
 0x20 : 'u',
 0x21 : '[',
 0x22 : 'i',
 0x23 : 'p',
 0x25 : 'l',
 0x26 : 'j',
 0x27 : '\'',
 0x28 : 'k',
 0x29 : ';',
 0x2a : '\\',
 0x2b : ',',
 0x2c : '/',
 0x2d : 'n',
 0x2e : 'm',
 0x2f : '.',
 0x32 : '`',
 0x31 : ' ',
 0x24 : '\r',
 0x30 : '\t',
 0x24 : '\n',
 0x24 : 'return' ,
 0x30 : 'tab' ,
 0x31 : 'space' ,
 0x33 : 'delete' ,
 0x35 : 'escape' ,
 0x37 : 'command' ,
 0x38 : 'shift' ,
 0x39 : 'capslock' ,
 0x3A : 'option' ,
 0x3A : 'alternate' ,
 0x3B : 'control' ,
 0x3C : 'rightshift' ,
 0x3D : 'rightoption' ,
 0x3E : 'rightcontrol' ,
 0x3F : 'function' ,
}

class KeyLogger(PyKeyboardEvent):
    def __init__(self,wLocation):
        PyKeyboardEvent.__init__(self)
        self._startTime = time.time()
        self._lastEventTime = self._startTime
        self._writeLocation = wLocation
        self._keyEventList = []

    @property
    def writeLocation(self):
        """Location of file where mouse click events will be written."""
        return self._writeLocation

    @writeLocation.setter
    def writeLocation(self, value):
        self._writeLocation = value

    @property
    def lastEventTime(self):
        """Time last event occurred."""
        return self._lastEventTime

    @property
    def startTime(self):
        """Time first event occurred."""
        return self._startTime

    @property
    def keyEventList(self):
        """List of x and y coordiantes for mouse clicks."""
        return self._keyEventList

    @keyEventList.setter
    def keyEventList(self, value):
        self._keyEventList = value

    def elapsedTime(self):
        elapsedTime = time.time() - self._startTime
        self._lastEventTime = time.time()
        return elapsedTime

    def stop(self):
        self.state = False #set listener loop to end
        self._writeKeyEventList()

    def _logEvent(self,key,eventType):
        time = self.elapsedTime()
        keyAndTime = [time,key_code_translate_table[key],eventType]
        self._keyEventList.append(keyAndTime)

    def key_press(self,key):
        if(self.state == True): #only accept inputs if loop is running
            if(key_code_translate_table[key] == 'escape'):
                self.stop()
            self._logEvent(key,'down')
        else:
            pass #do nothing

    def key_release(self,key):
        if(self.state == True): #only accept inputs if loop is running
            self._logEvent(key,'up')
        pass

    def _writeKeyEventList(self):
        if self._writeLocation:
            with open(self._writeLocation, 'wb') as f:
                pickle.dump(self._keyEventList,f)
        else:
            with open('test.txt', 'wb') as f:
                pickle.dump(self._keyEventList,f)

    def run(self):
        PyKeyboardEvent.run(self)
