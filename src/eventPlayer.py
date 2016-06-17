
import threading
import csv
from keyPlayer import KeyPlayer
from clickPlayer import ClickPlayer

class EventPlayer(object):
    def __init__(self):
        object.__init__(self)
        self._readLocation = ""
        self._eventList = []
        self._keyPlayer = KeyPlayer(self._readLocation)
        self._clickPlayer = ClickPlayer(self._readLocation)

    @property
    def readLocation(self):
        """Location of file containing series of events."""
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

    def _filterEventList(self, eventList, eventKeyword):
        filteredEventList = []
        for event in eventList:
            if event["eventType"] == eventKeyword:
                filteredEventList.append(event)
        return filteredEventList

    def _filterKeyEvents(self, eventList):
        return self._filterEventList(eventList, "key")

    def _filterClickEvents(self, eventList):
        return self._filterEventList(eventList, "click")

    def play(self, keyList, clickList):
        kp = KeyPlayer()
        kp.loadEventList(keyList)

        cp = ClickPlayer()
        cp.loadEventList(clickList)

        try:
            t1 = threading.Thread(target=kp.play)
            t2 = threading.Thread(target=cp.play)
            t1.start()
            t2.start()

            t1.join()
            t2.join()
        #    print "starting thread!"
        #kp.play()
            #thread.start_new_thread( kp.play, ())
        except:
            print "Error: unable to start KeyPlayer thread."
        #Threading here
        #kp.play()
        #cp.play()

    def printEventList(self):
        for item in self._eventList:
            print item
