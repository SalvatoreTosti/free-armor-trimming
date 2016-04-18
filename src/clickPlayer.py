import time
from numbers import Number
from collections import deque
from pymouse import PyMouse
import pickle

class ClickPlayer(PyMouse):
    def __init__(self,readLocation):
        PyMouse.__init__(self)
        self._readLocation = readLocation
        self._eventQueue = deque()

    @property
    def readLocation(self):
        """Location of file containing series of mouse click events."""
        return self._readLocation

    @readLocation.setter
    def readLocation(self,value):
        self._readLocation = value

    @property
    def eventQueue(self):
        """Queue of mouse click events."""
        return self._eventQueue

    @eventQueue.setter
    def eventQueue(self,value):
        self._eventQueue = value

    def click(self, x, y, button=1, n=1):
        PyMouse.click(self,x,y,button,n)

    def unpackEvent(self,event):
        if event:
            time = event[0]
            coordinates = event[1]
            x = coordinates[0]
            y = coordinates[1]
            assert isinstance(time,Number), "time is non-numeric, %r" % time
            assert isinstance(x,Number), "x is non-numeric, %r" % x
            assert isinstance(y,Number), "y is non-numeric, %r" % y
            return time,x,y
        else:
            return None

    def processEvent(self, waitTime, x, y):
        time.sleep(waitTime)
        self.click(x,y)

    def getNextEvent(self):
        if self._eventQueue:
            event = self._eventQueue.popleft()
            time,x,y = self.unpackEvent(event)
            self.processEvent(time,x,y)

    def addEvent(self, event):
        self._eventQueue.append(event)

    def play(self):
        self.readCoordinateList()
        while self._eventQueue:
            self.getNextEvent()

    def readCoordinateList(self):
        if self._readLocation:
            with open(self._readLocation,'rb') as f:
                rawList = pickle.load(f)
                for item in rawList:
                    self.addEvent(item)
        else:
            with open('test.txt','rb') as f:
                rawList = pickle.load(f)
                for item in rawList:
                    self.addEvent(item)
