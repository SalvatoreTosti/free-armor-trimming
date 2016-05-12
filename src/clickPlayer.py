import time
from numbers import Number
from collections import deque
from pymouse import PyMouse
import pickle
import csv

class ClickPlayer(PyMouse):
    def __init__(self, readLocation):
        PyMouse.__init__(self)
        self._readLocation = readLocation
        self._eventQueue = deque()
        self._readCoordinateList()

    @property
    def readLocation(self):
        """Location of file containing series of mouse click events."""
        return self._readLocation

    @readLocation.setter
    def readLocation(self, value):
        self._readLocation = value

    @property
    def eventQueue(self):
        """Queue of mouse click events."""
        return self._eventQueue

    @eventQueue.setter
    def eventQueue(self, value):
        self._eventQueue = value

    def click(self, x, y, button=1, n=1):
        PyMouse.click(self,x,y,button,n)

    def _unpackEvent(self, event):
        if event:
            if isinstance(event,dict):
                return self._unpackEventDict(event)
            elif isinstance(event,list):
                return self._unpackEventList(event)
            else:
                return self._unpackEventList(event)
        else:
            return None

    def _unpackEventDict(self, event):
        time = event['time']
        x = event['x']
        y = event['y']
        assert isinstance(time,Number), "time is non-numeric, %r" % time
        assert isinstance(x,Number), "x is non-numeric, %r" % x
        assert isinstance(y,Number), "y is non-numeric, %r" % y
        return time,x,y

    def _unpackEventList(self, event):
        time = event[0]
        x = event[1]
        y = event[2]
        assert isinstance(time,Number), "time is non-numeric, %r" % time
        assert isinstance(x,Number), "x is non-numeric, %r" % x
        assert isinstance(y,Number), "y is non-numeric, %r" % y
        return time,x,y

    def _processEvent(self, eventTime, x, y):
        nextTime = self._startTime + eventTime
        while(time.time() < nextTime):
            time.sleep(.001)
        self.click(x,y)

    def _getNextEvent(self):
        if self._eventQueue:
            event = self._eventQueue.popleft()
            time,x,y = self._unpackEvent(event)
            self._processEvent(time,x,y)

    def _addEvent(self, event):
        self._eventQueue.append(event)

    def play(self):
        self._readCoordinateList()
        self._startTime =  time.time()
        while self._eventQueue:
            self._getNextEvent()

    def _readCoordinateList(self):
        if self._readLocation:
            try:
                with open(self._readLocation,'rb') as f:
                    reader = csv.reader(f, delimiter=',', quotechar='|')
                    for row in reader:
                        lst = list(row)
                        event = [float(lst[1]),float(lst[2]),float(lst[3])]
                        self._addEvent(event)
            except EOFError:
                print str("Attempted to read invalid file: " + self._readLocation)
        else:
            pass #if no read location do nothing

    def printEventList(self):
        eventList = list(self._eventQueue)
        for event in eventList:
            print event
