from pymouse import PyMouseEvent
import time
import pickle
import csv

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
    def coordinateList(self):
        """List of x and y coordiantes for mouse clicks."""
        return self._coordinateList

    @coordinateList.setter
    def coordinateList(self, value):
        self._coordinateList = value

    def _elapsedTime(self):
        elapsedTime = time.time() - self._startTime
        self._lastEventTime = time.time()
        return elapsedTime

    def printCoordinateList(self):
        for item in self._coordinateList:
            print item
        print ""

    def click(self, x, y, button, press):
        coordinates = [x,y]
        time = self._elapsedTime()
        coordinatesAndTime = [time, x, y]
        self._coordinateList.append(coordinatesAndTime)

    def _writeCoordinateList(self):
        if self._writeLocation:
            with open(self._writeLocation, 'wb') as f:
                eventWriter = csv.writer(f, delimiter=',',
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for event in self._coordinateList:
                    time = event[0]
                    x = event[1]
                    y = event[2]
                    eventWriter.writerow([time,x,y])
        else:
            with open('test.txt', 'wb') as f:
                eventWriter = csv.writer(f, delimiter=',',
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for event in self._coordinateList:
                    time = event[0]
                    x = event[1]
                    y = event[2]
                    eventWriter.writerow([time,x,y])

    def run(self):
        #inspired by this guide on python automation https://automatetheboringstuff.com/chapter18/
        try:
            PyMouseEvent.run(self)
        except KeyboardInterrupt:
            self._writeCoordinateList()
