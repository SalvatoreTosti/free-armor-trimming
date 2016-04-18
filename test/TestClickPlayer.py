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
        self.assertEqual(None,cp.unpackEvent(None))

    def test_unpackEvent_small_vector(self):
        cp = ClickPlayer("")
        with self.assertRaises(IndexError) as cm:
            cp.unpackEvent(["test"])
        self.assertEqual('list index out of range',str(cm.exception))

        with self.assertRaises(IndexError) as cm:
            cp.unpackEvent(["test",[1]])
        self.assertEqual('list index out of range',str(cm.exception))

    def test_unpackEvent_invalid_values(self):
        cp = ClickPlayer("")
        with self.assertRaises(AssertionError) as cm:
            cp.unpackEvent(["test",[1,2]])
        self.assertEqual('time is non-numeric, \'test\'',str(cm.exception))

        with self.assertRaises(AssertionError) as cm:
            cp.unpackEvent([1,['a',3]])
        self.assertEqual('x is non-numeric, \'a\'',str(cm.exception))

        with self.assertRaises(AssertionError) as cm:
            cp.unpackEvent([1,[2,'b']])
        self.assertEqual('y is non-numeric, \'b\'',str(cm.exception))

    def test_unpackEvent_valid_values(self):
        cp = ClickPlayer("")
        self.assertEqual((1,2,3),cp.unpackEvent([1,[2,3]]))
        self.assertEqual((1.0,2.0,3.0),cp.unpackEvent([1.0,[2.0,3.0]]))

    def test_addEvent_None(self):
        cp = ClickPlayer("")
        cp.addEvent(None)
        dq = deque()
        self.assertEqual(dq.append(None),cp.eventQueue)
        #cp.addEvent([1,[2,3]])

        #self.assertEqual(deque([[1,[2,3]]]),cp.eventQueue)

if __name__ == '__main__':
    unittest.main()
