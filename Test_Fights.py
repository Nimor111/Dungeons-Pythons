import unittest
from Fights import Fights
from Hero import Hero
from Enemies import Enemy
from Weapon import Weapon
from Spell import Spell


class TestFight(unittest.TestCase):

    def setUp(self):
        self.fight = Fights(Hero(), Enemy())

    def test_fight_init(self):
        self.assertEqual(self.fight.hero.name, "Bron")
        self.assertEqual(self.fight.enemy.max_health, 100)
        self.assertTrue(self.fight.hero.equip(Weapon()))
        self.assertTrue(self.fight.hero.equip(Spell()))


if __name__ == '__main__':
    unittest.main()
