import unittest
from Hero import Hero


class TestHero(unittest.TestCase):

    def setUp(self):
        self.hero = Hero()

    def test_hero_init(self):
        self.assertEqual(self.hero.name, "Bron")
        self.assertEqual(self.hero.title, "Dragonslayer")
        self.assertEqual(self.hero.max_health, 100)
        self.assertEqual(self.hero.max_mana, 100)
        self.assertEqual(self.hero.mana_regeneration_rate, 2)
        self.assertEqual(self.hero.curr_health, 100)
        self.assertEqual(self.hero.curr_mana, 100)

    def test_known_as(self):
        self.assertEqual(self.hero.known_as(), "Bron the Dragonslayer")

    def test_get_health(self):
        self.assertEqual(self.hero.get_health(), 100)

    def test_get_mana(self):
        self.assertEqual(self.hero.get_mana(), 100)

    def test_is_alive(self):
        self.assertTrue(self.hero.is_alive())

    def test_can_cast(self):
        self.assertTrue(self.hero.can_cast())


if __name__ == "__main__":
    unittest.main()
