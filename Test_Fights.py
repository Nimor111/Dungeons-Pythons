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
        self.assertTrue(self.fight.hero.spell(
            Spell(name="Fireball", damage=20,
                  mana_cost=20, cast_range=2)))

    def test_fight(self):
        self.fight.hero.equip(Weapon())
        self.fight.hero.spell(Spell(name="Fireball", damage=20,
                              mana_cost=20, cast_range=2))
        self.assertEqual(self.fight.fight(), "Enemy is dead.")


if __name__ == '__main__':
    unittest.main()
