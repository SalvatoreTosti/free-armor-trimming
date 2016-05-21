import unittest
import sys
sys.path.append('../src/')

from eventEditor import EventEditor

class TestClickPlayer(unittest.TestCase):

    def test_initial_readLocation_None(self):
        ed = EventEditor(None)
        self.assertEqual(None,ed.readLocation)

    def test_initial_readLocation(self):
        ed = EventEditor("")
        self.assertEqual('',ed.readLocation)

    def test_initial_eventList(self):
        ed = EventEditor("")
        self.assertEqual([],ed.eventList)

    def test_set_readLocation(self):
        ed = EventEditor("")
        ed.readLocation = "test.txt"
        self.assertEqual("test.txt",ed.readLocation)

    def test_set_eventList(self):
        ed = EventEditor("")
        ed.eventList = ["a"]
        self.assertEqual(["a"],ed.eventList)

    def test_append_eventList(self):
        ed = EventEditor("")
        ed.eventList.append("a")
        self.assertEqual(["a"],ed.eventList)

    def test_ChangeEventTime_None(self):
        with self.assertRaises(AssertionError) as cm:
            ed = EventEditor("")
            newEvent = ed._changeEventTime(None,[0,200,300])
        self.assertEqual('newTime is non-numeric, None',str(cm.exception))

    def test_ChangeEventTime_Non_Numeric(self):
        with self.assertRaises(AssertionError) as cm:
            ed = EventEditor("")
            newEvent = ed._changeEventTime("a",[0,200,300])
        self.assertEqual('newTime is non-numeric, \'a\'',str(cm.exception))

    def test_ChangeEventTime(self):
        ed = EventEditor("")
        newEvent = ed._changeEventTime(2,{ "eventType" : "click" , "time" : 0, "x" : 200, "y" : 300 })
        self.assertEqual({ "eventType" : "click" , "time" : 2, "x" : 200, "y" : 300 },newEvent)

    def test_changeEventX_Non_Numeric(self):
        with self.assertRaises(AssertionError) as cm:
            ed = EventEditor("")
            newEvent = ed._changeEventX("a",[0,200,300])
        self.assertEqual('newX is non-numeric, \'a\'',str(cm.exception))

    def test_changEventX_None(self):
        with self.assertRaises(AssertionError) as cm:
            ed = EventEditor("")
            newEvent = ed._changeEventX(None,[0,200,300])
        self.assertEqual('newX is non-numeric, None',str(cm.exception))

    def test_changeEventX(self):
        ed = EventEditor("")
        newEvent = ed._changeEventX(2,{ "eventType" : "click" , "time" : 0, "x" : 200, "y" : 300 })
        self.assertEqual({ "eventType" : "click" , "time" : 0, "x" : 2, "y" : 300 },newEvent)

    def test_changeEventY_Non_Numeric(self):
        with self.assertRaises(AssertionError) as cm:
            ed = EventEditor("")
            newEvent = ed._changeEventY("a",[0,200,300])
        self.assertEqual('newY is non-numeric, \'a\'',str(cm.exception))

    def test_changEventY_None(self):
        with self.assertRaises(AssertionError) as cm:
            ed = EventEditor("")
            newEvent = ed._changeEventY(None,[0,200,300])
        self.assertEqual('newY is non-numeric, None',str(cm.exception))

    def test_changeEventY(self):
        ed = EventEditor("")
        newEvent = ed._changeEventY(2,{ "eventType" : "click" , "time" : 0, "x" : 200 , "y" : 300 })
        self.assertEqual({ "eventType" : "click" , "time" : 0, "x" : 200 , "y" : 2 },newEvent)

    def test_moveEvent_Bad_Location_High(self):
        ed = EventEditor("")
        ed.eventList =["a","b","c"]
        ed._moveEvent(1,5)
        self.assertEqual(["a","c","b"],ed.eventList)

    def test_moveEvent_Bad_Location_Low(self):
        ed = EventEditor("")
        ed.eventList =["a","b","c"]
        ed._moveEvent(1,-5)
        self.assertEqual(["b","a","c"],ed.eventList)

    def test_moveEvent(self):
        ed = EventEditor("")
        ed.eventList =["a","b","c"]
        ed._moveEvent(1,0)
        self.assertEqual(["b","a","c"],ed._eventList)
        ed.eventList = ["a","b","c"]
        ed._moveEvent(2,0)
        self.assertEqual(["c","a","b"],ed._eventList)
        ed.eventList = ["a","b","c"]

    def test_moveEvent_Same_Location(self):
        ed = EventEditor("")
        ed.eventList = ["a","b","c"]
        ed._moveEvent(0,0)
        self.assertEqual(["a","b","c"],ed._eventList)
        ed.eventList = ["a","b","c"]
        ed._moveEvent(1,1)
        self.assertEqual(["a","b","c"],ed._eventList)
        ed.eventList = ["a","b","c"]
        ed._moveEvent(2,2)
        self.assertEqual(["a","b","c"],ed._eventList)

    def test_readEventList_Bad_Location(self):
        with self.assertRaises(IOError) as cm:
            ed = EventEditor("doesnt-exist.txt")
            ed._readEventList(ed.readLocation)
        self.assertEqual('[Errno 2] No such file or directory: \'doesnt-exist.txt\'',str(cm.exception))

    def test_readEventList_Bad_Location(self):
        with self.assertRaises(IOError) as cm:
            ed = EventEditor("doesnt-exist.txt")
            ed._readEventList(ed.readLocation)
        self.assertEqual('[Errno 2] No such file or directory: \'doesnt-exist.txt\'',str(cm.exception))

if __name__ == '__main__':
    unittest.main()
