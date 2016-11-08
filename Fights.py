from Hero import Hero
from Enemies import Enemy
from Weapon import Weapon


class Fights:

    def __init__(self, hero, enemy):
        if type(hero) != Hero:
            raise TypeError("Must be a hero!")
        if type(enemy) != Enemy:
            raise TypeError("Must be an enemy!")
        self.hero = hero
        self.hero.equip(Weapon())
        self.enemy = enemy

    def start_fight(self):
        return " A fight has started between our Hero(health={}, mana={}) and \
an Enemy(health={}, mana={}, damage={}) " \
            .format(self.hero.get_health(), self.hero.get_mana(),
                    self.enemy.get_health(), self.enemy.get_mana(),
                    self.enemy.damage)

    def hero_turn(self):


    def enemy_turn(self):
        pass

    def fight(self):
        pass


def main():
    fight = Fights(Hero(), Enemy())
    print(fight.start_fight())
    print(fight.hero_turn())


if __name__ == "__main__":
    main()
