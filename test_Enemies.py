import unittest
from Enemies import Enemy


class testEnemies(unittest.TestCase):
    def setUp(self):
        self.enemy = Enemy()
        self.enemy1 = Enemy(0, 0, 0)

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


if __name__ == '__main__':
    unittest.main()
