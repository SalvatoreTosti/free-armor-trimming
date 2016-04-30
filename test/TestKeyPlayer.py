import unittest
import sys
sys.path.append('../src/')

from keyPlayer import KeyPlayer
from collections import deque

class TestKeyPlayer(unittest.TestCase):

    def test_initial_queue(self):
        kp = KeyPlayer("")
        self.assertEqual(deque(),kp.eventQueue)

    def test_initial_readLocation_None(self):
        kp = KeyPlayer(None)
        self.assertEqual(None,kp.readLocation)

    def test_initial_readLocation(self):
        kp = KeyPlayer("")
        self.assertEqual('',kp.readLocation)

    def test_unpackEvent_None(self):
        kp = KeyPlayer("")
        self.assertEqual(None,kp._unpackEvent(None))

    def test_unpackEvent_None_list(self):
        kp = KeyPlayer("")
        event = []
        self.assertEqual(None,kp._unpackEvent(event))

    def test_unpackEvent_invalid_values_list(self):
        kp = KeyPlayer("")
        with self.assertRaises(IndexError) as cm:
            kp._unpackEvent(["time"])
        self.assertEqual('list index out of range',str(cm.exception))

        with self.assertRaises(IndexError) as cm:
            kp._unpackEvent(["time","key"])
        self.assertEqual('list index out of range',str(cm.exception))

        with self.assertRaises(AssertionError) as cm:
            kp._unpackEvent(["time","key","event"])
        self.assertEqual('time is non-numeric, \'time\'',str(cm.exception))

        with self.assertRaises(AssertionError) as cm:
            kp._unpackEvent([1.0,2,"event"])
        self.assertEqual('key is not a string, 2',str(cm.exception))

        with self.assertRaises(AssertionError) as cm:
            kp._unpackEvent([1.0,'a',3])
        self.assertEqual('eventType is not a string, 3',str(cm.exception))

    def test_unpackEvent_valid_values_list(self):
        kp = KeyPlayer("")
        self.assertEqual((1,'a','up'),kp._unpackEvent([1.0,'a','up']))
        self.assertEqual((1.0,'a','down'),kp._unpackEvent([1.0,'a','down']))

    def test_unpackEvent_None_map(self):
        kp = KeyPlayer("")
        event = {}
        self.assertEqual(None,kp._unpackEvent(event))

    def test_unpackEvent_invalid_values_map(self):
        kp = KeyPlayer("")
        with self.assertRaises(KeyError) as cm:
            event = {'time': 1, 'key': 'a'}
            kp._unpackEvent(event)

    def test_unpackEvent_valid_values_map(self):
        kp = KeyPlayer("")
        event = {'time': 1, 'key': 'a', 'eventType': 'up'}
        self.assertEqual((1,'a','up'),kp._unpackEvent(event))

    def test_addEvent_None(self):
        kp = KeyPlayer("")
        kp._addEvent(None)
        dq = deque()
        dq.append(None)

        self.assertEqual(dq,kp.eventQueue)

if __name__ == '__main__':
    unittest.main()
