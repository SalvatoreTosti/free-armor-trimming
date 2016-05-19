import unittest
import sys
sys.path.append('../src/')

from clickPlayer import ClickPlayer
from collections import deque

class TestClickPlayer(unittest.TestCase):

    def test_initial_queue(self):
        cp = ClickPlayer("")
        self.assertEqual(deque(),cp.eventQueue)

    def test_initial_readLocation_None(self):
        cp = ClickPlayer(None)
        self.assertEqual(None,cp.readLocation)

    def test_initial_readLocation(self):
        cp = ClickPlayer("")
        self.assertEqual('',cp.readLocation)

    def test_unpackEvent_None(self):
        cp = ClickPlayer("")
        self.assertEqual(None,cp._unpackEvent(None))

    def test_unpackEvent_None_list(self):
        cp = ClickPlayer("")
        event = []
        self.assertEqual(None,cp._unpackEvent(event))

    def test_unpackEvent_invalid_values_list(self):
        cp = ClickPlayer("")
        with self.assertRaises(IndexError) as cm:
            cp._unpackEvent(["test"])
        self.assertEqual('list index out of range',str(cm.exception))

        with self.assertRaises(IndexError) as cm:
            cp._unpackEvent(["test",[1]])
        self.assertEqual('list index out of range',str(cm.exception))

        with self.assertRaises(AssertionError) as cm:
            cp._unpackEvent(["test",1,2])
        self.assertEqual('time is non-numeric, \'test\'',str(cm.exception))

        with self.assertRaises(AssertionError) as cm:
            cp._unpackEvent([1,'a',3])
        self.assertEqual('x is non-numeric, \'a\'',str(cm.exception))

        with self.assertRaises(AssertionError) as cm:
            cp._unpackEvent([1,2,'b'])
        self.assertEqual('y is non-numeric, \'b\'',str(cm.exception))

    def test_unpackEvent_valid_values_list(self):
        cp = ClickPlayer("")
        self.assertEqual((1,2,3),cp._unpackEvent([1,2,3]))
        self.assertEqual((1.0,2.0,3.0),cp._unpackEvent([1.0,2.0,3.0]))

    def test_unpackEvent_None_map(self):
        cp = ClickPlayer("")
        event = {}
        self.assertEqual(None,cp._unpackEvent(event))

    def test_unpackEvent_invalid_values_map(self):
        cp = ClickPlayer("")
        with self.assertRaises(KeyError) as cm:
            event = {'time': 1, 'x': 2}
            cp._unpackEvent(event)

    def test_unpackEvent_valid_values_map(self):
        cp = ClickPlayer("")
        event = {'time': 1, 'x': 2, 'y':3}
        self.assertEqual((1,2,3),cp._unpackEvent(event))

    def test_addEvent_None(self):
        cp = ClickPlayer("")
        cp._addEvent(None)
        dq = deque()
        dq.append(None)

        self.assertEqual(dq,cp.eventQueue)

if __name__ == '__main__':
    unittest.main()
