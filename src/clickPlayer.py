import time
from pymouse import PyMouse

class clickPlayer(PyMouse):
    def click(self, x, y, button=1,n=1):
        PyMouse.click(self,x,y,button,n)
    def processNextEvent(self,waitTime, x, y):
        time.sleep(waitTime)
        self.click(x,y)
