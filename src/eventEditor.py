from numbers import Number
import csv

class EventEditor(object):
    def __init__(self, readLocation):
        object.__init__(self)
        self._readLocation = readLocation
        self._eventList = []
        self._readEventList(self._readLocation)

    @property
    def readLocation(self):
        """Location of file containing series of mouse or keyboard events."""
        return self._readLocation

    @readLocation.setter
    def readLocation(self, value):
        self._readLocation = value

    @property
    def eventList(self):
        """Queue of mouse or keyboard events events."""
        return self._eventList

    @eventList.setter
    def eventList(self, value):
        self._eventList = value

    def _addEvent(self, event):
        self._eventList.append(event)

    def _changeEventTime(self,newTime,event):
        assert isinstance(newTime,Number), "newTime is non-numeric, %r" % newTime
        x = event[1]
        y = event[2]
        return [newTime,x,y]

    def _changeEventX(self,newX,event):
        assert isinstance(newX,Number), "newX is non-numeric, %r" % newX
        time = event[0]
        y = event[2]
        return [time,newX,y]

    def _changeEventY(self,newY,event):
        assert isinstance(newY,Number), "newY is non-numeric, %r" % newY
        time = event[0]
        x = event[1]
        return [time,x,newY]

    def _moveEvent(self, oldPosition, newPosition):
        event = self._eventList.pop(oldPosition)
        self._eventList.insert(newPosition, event)

    def printEventList(self):
        for item in self._eventList:
            print item
        print ""

    def _readEventList(self,readLocation):
        if readLocation:
            try:
                with open(readLocation,"rb") as f:
                    reader = csv.reader(f,delimiter=",",quotechar="|")
                    for row in reader:
                        lst = list(row)
                        eventType = lst[0]
                        if eventType == "key":
                            event = [float(lst[1]),lst[2],lst[3]]
                        else:
                            event = [float(lst[1]),float(lst[2]),float(lst[3])]
                        self._addEvent(event)
            except EOFError:
                print str("Attempted to read invalid file: " + readLocation)
        else:
            pass #if no read location do nothing
