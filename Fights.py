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
        weapon = Weapon(name="Claws", damage=5)
        self.enemy.equip(weapon)
        print(self.enemy.weapons)

    def start_fight(self):
        return " A fight has started between our Hero(health={}, mana={}) and \
an Enemy(health={}, mana={}, damage={}) " \
            .format(self.hero.get_health(), self.hero.get_mana(),
                    self.enemy.get_health(), self.enemy.get_mana(),
                    self.enemy.damage)

    def find_max_attr(self, types, hero):
        attr_type = []
        if types == "spell":
            attr_type = hero.spells
        elif types == "weapon":
            attr_type = hero.weapons
        else:
            raise TypeError("Must be weapon or spell!")

        if attr_type != []:
            max_attr_dmg = max([(attr, attr.damage)
                                for attr in attr_type])
            return max_attr_dmg[0]
        else:
            return "Error!"

    def turn(self, hero, enemy, hero_str, enemy_str):
        if hero.is_alive() is False:
            return "Error. {} is dead.".format(hero_str)
        if enemy.is_alive() is False:
            return "{} is dead.".format(enemy_str)
        max_spell = self.find_max_attr("spell", hero)
        if hero.can_cast() is False:
            return "{} does not have enough mana for another {}" \
                .format(hero_str, max_spell.name)
        if hero.spells != []:
            if hero.can_cast_spell(max_spell):
                enemy.cur_health -= max_spell.damage
                return "{} casts a {}, hits {} for {} dmg. \
{} health is {}".format(hero_str, max_spell.name, enemy_str,
                        hero.attack(magic=max_spell.name), enemy_str,
                        enemy.cur_health)
        elif hero.weapons != []:
            max_weapon = self.find_max_attr("weapon", hero)
            enemy.cur_health -= max_weapon.damage
            return "{} hits with {} for {} dmg. {} health is {}" \
                .format(hero_str, max_weapon.name,
                        max_weapon.damage, enemy_str,
                        enemy.cur_health)

    def hero_turn(self):
        return self.turn(self.hero, self.enemy, "Hero", "Enemy")

    def enemy_turn(self):
        return self.turn(self.enemy, self.hero, "Enemy", "Hero")

    def fight(self):
        pass


def main():
    fight = Fights(Hero(), Enemy())
    print(fight.start_fight())
    print(fight.hero_turn())
    print(fight.enemy_turn())
    print(fight.hero_turn())
    print(fight.enemy_turn())
    print(fight.hero_turn())
    print(fight.enemy_turn())
    print(fight.hero_turn())
    print(fight.enemy_turn())
    print(fight.hero_turn())
    print(fight.enemy_turn())


if __name__ == "__main__":
    main()
