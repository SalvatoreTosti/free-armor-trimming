import pymouse
import pykeyboard
import time

class clickLogger(pymouse.PyMouseEvent):
    startTime = time.time()
    coordinateList = []
    def __init__(self):
        pymouse.PyMouseEvent.__init__(self)
    def elapsedTime(self):
        return time.time() - self.startTime
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

class keyLogger(pykeyboard.PyKeyboardEvent):
    def __init__(self):
        pykeyboard.PyKeyboardEvent.__init__(self)
    def tap(self, keycode, character, press):
        print character
    def run(self):
        pykeyboard.PyKeyboardEvent.run(self)

mouse = pymouse.PyMouse()
print mouse.position()
#mouse.click(100,100)

event =  pymouse.PyMouseEvent();

klogger = keyLogger()
#klogger.run()
#logger = clickLogger()
#logger.run()
