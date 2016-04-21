from pymouse import PyMouseEvent
import time
import pickle

class ClickLogger(PyMouseEvent):
    def __init__(self,wLocation):
        PyMouseEvent.__init__(self)
        self._startTime = time.time()
        self._lastEventTime = self._startTime
        self._writeLocation = wLocation
        self._coordinateList = []

    @property
    def writeLocation(self):
        """Location of file where mouse click events will be written."""
        return self._writeLocation

    @writeLocation.setter
    def writeLocation(self,value):
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
    def coordinateList(self):
        """List of x and y coordiantes for mouse clicks."""
        return self._coordinateList

    @coordinateList.setter
    def coordinateList(self,value):
        self._coordinateList = value

    def elapsedTime(self):
        elapsedTime = time.time() - self._lastEventTime
        self._lastEventTime = time.time()
        return elapsedTime

    def printCoordinateList(self):
        for item in self._coordinateList:
            print item
        print ""

    def click(self,x,y,button,press):
        coordinates = [x,y]
        time = self.elapsedTime()
        coordinatesAndTime = [time, coordinates]
        self._coordinateList.append(coordinatesAndTime)
        self.writeCoordinateList()

    def writeCoordinateList(self):
        if self._writeLocation:
            with open(self._writeLocation, 'wb') as f:
                pickle.dump(self._coordinateList,f)
        else:
            with open('test.txt', 'wb') as f:
                pickle.dump(self._coordinateList,f)
