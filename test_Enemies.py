import unittest
from Enemies import Enemy


class testEnemies(unittest.TestCase):
    def setUp(self):
        self.enemy = Enemy()
        self.enemy1 = Enemy(0, 0, 0)
        self.enemy2 = Enemy(0, 200, 0)

    def test_is_alive(self):
        self.assertTrue(self.enemy.is_alive())
        self.assertFalse(self.enemy1.is_alive())

    def test_can_cast(self):
        self.assertTrue(self.enemy.can_cast())
        self.assertFalse(self.enemy1.can_cast())

    def test_get_health(self):
        self.assertEqual(self.enemy.get_health(), 100)
        self.assertEqual(self.enemy1.get_health(), 0)

    def test_get_mana(self):
        self.assertEqual(self.enemy.get_mana(), 100)
        self.assertEqual(self.enemy1.get_mana(), 0)

    def test_take_healing(self):
        self.assertTrue(self.enemy.take_healing(10))
        self.assertFalse(self.enemy1.take_healing(10))

    def test_take_mana(self):
        self.assertEqual(self.enemy.take_mana(100), 100)
        self.assertEqual(self.enemy2.take_mana(1), 200)


if __name__ == '__main__':
    unittest.main()
