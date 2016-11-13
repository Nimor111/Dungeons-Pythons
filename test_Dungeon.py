import unittest
from Dungeons import Dungeon


class testDungeon(unittest.TestCase):
    def setUp(self):
        self.d1 = Dungeon("test.txt")

    def test_spawn(self):
        self.assertEqual(self.d1.spawn(), ["H.##.....T",
                                           "#T##..###.",
                                           "#.###E###E",
                                           "#.E...###.",
                                           "###T#####G"])

    def test_validate(self):
        self.d1.spawn()
        self.assertFalse(self.d1.validate("left"))
        self.assertTrue(self.d1.validate("right"))
        self.assertFalse(self.d1.validate("up"))
        self.assertFalse(self.d1.validate("down"))

    def test_movement(self):

if __name__ == '__main__':
    unittest.main()
