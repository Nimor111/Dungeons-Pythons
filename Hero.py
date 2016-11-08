from Weapon import Weapon
from Spell import Spell


class Hero:

    def __init__(self, name="Bron", title="Dragonslayer", max_health=100,
                 max_mana=100, mana_regeneration_rate=2):
        self.name = name
        self.title = title
        self.max_health = self.curr_health = max_health
        self.max_mana = self.curr_mana = max_mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.weapons = []
        self.spells = []

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def get_health(self):
        return self.curr_health

    def get_mana(self):
        return self.curr_mana

    def is_alive(self):
        return self.curr_health > 0

    def can_cast(self):
        return self.curr_mana > 0

    def take_damage(self, damage_points):
        if self.curr_health - damage_points > 0:
            self.curr_health = self.curr_health - damage_points
            return self.curr_health
        else:
            return 0

    def take_healing(self, healing_points):
        if self.is_alive() is False:
            return False
        elif self.curr_health + healing_points > self.curr_health:
            self.curr_health = self.max_health
            return self.curr_health
        else:
            self.curr_health += healing_points
            return self.curr_health

    def regen_mana(self):
        self.curr_mana += self.mana_regeneration_rate
        return self.curr_mana

    def can_cast_spell(self, spell):
        if self.can_cast() == 1:
            self.curr_mana -= spell.mana_cost
            return True
        else:
            return False

    def take_mana(self, mana_points):
        if self.curr_mana + mana_points > self.curr_mana:
            self.curr_mana = self.max_mana
            return self.curr_mana
        else:
            self.curr_mana += mana_points
            return self.curr_mana

    def equip(self, weapon):
        if type(weapon) == Weapon:
            self.weapons.append(weapon)
        else:
            return False

    def spell(self, spell):
        if type(spell) == Spell:
            self.spells.append(spell)
        else:
            return False

    def attack(self, **kwargs):
        if kwargs.keys[0] == "weapon":
            for weapon in self.weapons:
                if kwargs["weapon"] == weapon.name:
                    return weapon.damage
        elif kwargs.keys[0] == "magic":
            for spell in self.spells:
                if kwargs["magic"] == spell.name:
                    return spell.damage
        else:
            return 0
