from Hero import Hero
from Enemies import Enemy
from Weapon import Weapon
from Spell import Spell


class Fights:

    def __init__(self, hero, enemy):
        if type(hero) != Hero:
            raise TypeError("Must be a hero!")
        if type(enemy) != Enemy:
            raise TypeError("Must be an enemy!")
        self.hero = hero
        self.hero.equip(Weapon())
        self.hero.spell(Spell(name="Fireball", damage=20,
                              mana_cost=20, cast_range=2))
        self.enemy = enemy

    def start_fight(self):
        return " A fight has started between our Hero(health={}, mana={}) and \
an Enemy(health={}, mana={}, damage={}) " \
            .format(self.hero.get_health(), self.hero.get_mana(),
                    self.enemy.get_health(), self.enemy.get_mana(),
                    self.enemy.damage)

    def find_max_attr(self, types):
        attr_type = []
        if types == "spell":
            attr_type = self.hero.spells
        elif types == "weapon":
            attr_type = self.hero.weapons
        else:
            raise TypeError("Must be weapon or spell!")

        max_attr_dmg = max([(attr, attr.damage)
                           for attr in attr_type])
        return max_attr_dmg[0]

    def hero_turn(self):
        if self.enemy.is_alive() is False:
            return "Enemy is dead."
        max_spell = self.find_max_attr("spell")
        if self.hero.can_cast() is False:
            return "Hero does not have enough mana for another {}" \
                .format(max_spell.name)
        if self.hero.spells != []:
            if self.hero.can_cast_spell(max_spell):
                self.enemy.cur_health -= max_spell.damage
                return "Hero casts a {}, hits enemy for {} dmg. \
Enemy health is {}".format(max_spell.name, max_spell.damage,
                           self.enemy.cur_health)
        elif self.hero.weapons != []:
            max_weapon = self.find_max_attr("weapon")
            return "Hero hits with {} for {} dmg. Enemy health is {}" \
                .format(max_weapon.name, max_weapon.damage,
                        self.enemy.cur_health)

    def enemy_turn(self):
        pass

    def fight(self):
        pass


def main():
    fight = Fights(Hero(), Enemy())
    print(fight.start_fight())
    print(fight.hero_turn())
    print(fight.hero_turn())
    print(fight.hero_turn())
    print(fight.hero_turn())
    print(fight.hero_turn())
    print(fight.hero_turn())


if __name__ == "__main__":
    main()
