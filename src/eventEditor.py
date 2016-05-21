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
        event["time"] = newTime
        return event

    def _changeEventX(self,newX,event):
        assert isinstance(newX,Number), "newX is non-numeric, %r" % newX
        event["x"] = newX
        return event

    def _changeEventY(self,newY,event):
        assert isinstance(newY,Number), "newY is non-numeric, %r" % newY
        event["y"] = newY
        return event

    def _changeKey(self,newKey,event):
        assert isinstance(newKey,basestring), "newKey is non-string, %r" % newKey
        event["key"] = newKey
        return event

    def _changeKeyType(self,newKeyType,event):
        assert isinstance(newKeyType,basestring), "newKeytype is non-string, %r" % newKeyType
        event["keyType"] = newKeyType
        return event

    def _moveEvent(self, oldPosition, newPosition):
        event = self._eventList.pop(oldPosition)
        self._eventList.insert(newPosition, event)

    def printEventList(self):
        for item in self._eventList:
            print item

    def printNumberedEventList(self):
        row = 0
        for item in self._eventList:
            print str(row) + " " + str(item)
            row += 1

    def _readEventList(self,readLocation):
        if readLocation:
            try:
                with open(readLocation,"rb") as f:
                    reader = csv.reader(f,delimiter=",",quotechar="|")
                    for row in reader:
                        lst = list(row)
                        eventType = lst[0]
                        if eventType == "key":
                            event = { "eventType" : "key", "time" : float(lst[1]), "key" : lst[2], "keyType" : lst[3] }
                        else:
                            event = { "eventType" : "click", "time" : float(lst[1]), "x" : float(lst[2]), "y" : float(lst[3])}
                        self._addEvent(event)
            except EOFError:
                print str("Attempted to read invalid file: " + readLocation)
        else:
            pass #if no read location do nothing

    def _writeEventList(self,writeLocation):
        if writeLocation:
            with open(writeLocation, "wb") as f:
                eventWriter = csv.writer(f, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
                for event in self._eventList:
                        if(event["eventType"] == "click"):
                            eventWriter.writerow([event["eventType"], event["time"],
                            event["x"],event["y"]])
                        elif(event["eventType"] == "key"):
                            eventWriter.writerow([event["eventType"], event["time"],
                            event["key"], event["keyType"]])
