import unittest
from Dungeons import *


class testDungeon(unittest.TestCase):
    def setUp(self):
        self.d1 = Dungeon("test1.txt", "treasures.txt")

    def test_spawn(self):
        self.h = Hero("this", "that", 100, 100, 2)
        self.assertEqual(self.d1.spawn(self.h), ["H.##.....T",
                                                 "#T##..###.",
                                                 "#.###E###E",
                                                 "#.E...###.",
                                                 "###T#####G"])

    def test_validate(self):
        self.h = Hero("this", "that", 100, 100, 2)
        # self.d1.spawn(self.h)
        # self.assertFalse(self.d1.validate("left"))
        # self.assertTrue(self.d1.validate("right"))
        # self.assertFalse(self.d1.validate("up"))
        # self.assertFalse(self.d1.validate("down"))
        self.d1.i = 1
        self.d1.j = 0
        self.assertTrue(self.d1.validate("left"))
        self.assertTrue(self.d1.validate("right"))
        self.assertFalse(self.d1.validate("up"))
        self.assertTrue(self.d1.validate("down"))

if __name__ == '__main__':
    unittest.main()
