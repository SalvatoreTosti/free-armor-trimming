import time
from numbers import Number
from collections import deque
from pykeyboard import PyKeyboard
import pickle

class KeyPlayer(PyKeyboard):
    def __init__(self,readLocation):
        PyKeyboard.__init__(self)
        self._readLocation = readLocation
        self._eventQueue = deque()
        self._readKeyList()

    @property
    def readLocation(self):
        """Location of file containing series of key press events."""
        return self._readLocation

    @readLocation.setter
    def readLocation(self, value):
        self._readLocation = value

    @property
    def eventQueue(self):
        """Queue of key press events."""
        return self._eventQueue

    @eventQueue.setter
    def eventQueue(self, value):
        self._eventQueue = value

    def _key_down(self,character):
        self.press_key(character)

    def _key_up(self,character):
        self.release_key(character)

    def _unpackEvent(self,event):
        if event:
            if isinstance(event,dict):
                return self._unpackEventDict(event)
            elif isinstance(event,list):
                return self._unpackEventList(event)
            else:
                return self._unpackEventList(event)
        else:
            return None

    def _unpackEventDict(self,event):
        time = event['time']
        key = event['key']
        eventType = event['eventType']
        assert isinstance(time,Number), "time is non-numeric, %r" % time
        assert isinstance(key,str), "key is not a string, %r" % key
        assert isinstance(eventType,str), "eventType is not a string, %r" % eventType
        return time,key,eventType

    def _unpackEventList(self, event):
        time = event[0]
        key = event[1]
        eventType = event[2]
        assert isinstance(time,Number), "time is non-numeric, %r" % time
        assert isinstance(key,str), "key is not a string, %r" % key
        assert isinstance(eventType,str), "eventType is not a string, %r" % eventType
        return time,key,eventType

    def _processEvent(self, waitTime, key, eventType):
        time.sleep(waitTime)
        if(eventType == 'down'):
            self._key_down(key)
        elif(eventType == 'up'):
            self._key_up(key)
        else:
            raise ValueError('invalid eventType supplied.')

    def _getNextEvent(self):
        if self._eventQueue:
            event = self._eventQueue.popleft()
            time,key,eventType = self._unpackEvent(event)
            self._processEvent(time,key,eventType)

    def _addEvent(self,event):
        self._eventQueue.append(event)

    def play(self):
        self._readKeyList()
        while self._eventQueue:
            self._getNextEvent()

    def _readKeyList(self):
        if self._readLocation:
            try:
                with open(self._readLocation,'rb') as f:
                    rawList = pickle.load(f)
                    for item in rawList:
                        self._addEvent(item)
            except EOFError:
                print str("Attempted to read invalid file: " + self._readLocation)
        else:
            pass #if no read location do nothing

    def printEventList(self):
        eventList = list(self._eventQueue)
        for event in eventList:
            print event
