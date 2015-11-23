import time
from collections import deque
from pymouse import PyMouse
import pickle

class clickPlayer(PyMouse):
    eventQueue = deque()
    def click(self, x, y, button=1, n=1):
        PyMouse.click(self,x,y,button,n)

    def unpackEvent(self,event):
        time = event[0]
        print event[1]
        coordinates = event[1]
        x = coordinates[0]
        y = coordinates[1]
        return time,x,y

    def processEvent(self, waitTime, x, y):
        time.sleep(waitTime)
        self.click(x,y)

    def getNextEvent(self):
        if self.eventQueue:
            event = self.eventQueue.popleft()
            time,x,y = self.unpackEvent(event)
            self.processEvent(time,x,y)

    def addEvent(self, event):
        self.eventQueue.append(event)

    def play(self):
        while self.eventQueue:
            self.getNextEvent()

    def readCoordinateList(self):
        with open('test.txt','rb') as f:
            rawList = pickle.load(f)
            for item in rawList:
                self.addEvent(item)
