from pymouse import PyMouseEvent
import time

class clickLogger(PyMouseEvent):
    startTime = time.time()
    lastEventTime = startTime
    coordinateList = []
    def __init__(self):
        PyMouseEvent.__init__(self)
        startTime = time.time()
        lastEventTime = startTime

    def elapsedTime(self):
        elapsedTime = time.time() - self.lastEventTime
        self.lastEventTime = time.time()
        return elapsedTime

    def getCoordinateList(self):
        return self.coordinateList

    def printCoordinateList(self):
        for item in self.getCoordinateList():
            print item
        print ""

    def click(self,x,y,button,press):
        coordinates = [x,y]
        time = self.elapsedTime()
        coordinatesAndTime = [time, coordinates]
        self.coordinateList.append(coordinatesAndTime)
        self.printCoordinateList()
