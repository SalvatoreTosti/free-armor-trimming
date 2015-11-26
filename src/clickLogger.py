from pymouse import PyMouseEvent
import time
import pickle

class clickLogger(PyMouseEvent):
    startTime = time.time()
    lastEventTime = startTime
    coordinateList = []

    def __init__(self,wLocation):
        PyMouseEvent.__init__(self)
        startTime = time.time()
        lastEventTime = startTime
        self.writeLocation = wLocation

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
        self.writeCoordinateList()

    def writeCoordinateList(self):
        #print self.writeLocation
        if self.writeLocation:
            with open(self.writeLocation, 'wb') as f:
                pickle.dump(self.getCoordinateList(),f)
        else:
            with open('test.txt', 'wb') as f:
                pickle.dump(self.getCoordinateList(),f)
        #with open('test.txt', 'w') as f:
            #for coordinate in self.getCoordinateList():
                #print coordinate
                #f.write("%s\n" % str(coordinate))
