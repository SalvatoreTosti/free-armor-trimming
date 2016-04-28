import unittest
import sys
sys.path.append('../src/')

from keyLogger import KeyLogger

class TestKeyLogger(unittest.TestCase):

    def test_initial_startTime(self):
        kl = KeyLogger("")
        self.assertEqual(kl.lastEventTime,kl.startTime)

    def test_initial_lastEventTime(self):
        kl = KeyLogger("")
        self.assertEqual(kl.startTime,kl.lastEventTime)

    def test_initial_writeLocation(self):
        kl = KeyLogger("")
        self.assertEqual("",kl.writeLocation)
        kl = KeyLogger("test-file.txt")
        self.assertEqual("test-file.txt",kl.writeLocation)

    def test_initial_coordinateLocation(self):
        kl = KeyLogger("")
        self.assertEqual([],kl.keyPressList)

if __name__ == '__main__':
    unittest.main()
