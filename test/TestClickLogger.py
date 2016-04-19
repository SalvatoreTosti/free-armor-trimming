import unittest
import sys
sys.path.append('../src/')

from clickLogger import ClickLogger

class TestClickLogger(unittest.TestCase):

    def test_initial_startTime(self):
        cl = ClickLogger("")
        self.assertEqual(cl.lastEventTime,cl.startTime)

    def test_initial_lastEventTime(self):
        cl = ClickLogger("")
        self.assertEqual(cl.startTime,cl.lastEventTime)

    def test_initial_writeLocation(self):
        cl = ClickLogger("")
        self.assertEqual("",cl.writeLocation)

        cl = ClickLogger("test-file.txt")
        self.assertEqual("test-file.txt",cl.writeLocation)

    def test_initial_coordinateLocation(self):
        cl = ClickLogger("kk")
        self.assertEqual([],cl.coordinateList)

if __name__ == '__main__':
    unittest.main()
