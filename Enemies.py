from Spell import Spell
from Weapon import Weapon


class Enemy:
    def __init__(self, health=100, mana=100, damage=20):
        self.max_health = self.cur_health = health
        self.max_mana = self.cur_mana = mana
        self.damage = damage
        self.weapons = []
        self.spells = []

    def is_alive(self):
        return self.cur_health > 0

    def can_cast(self):
        return self.cur_mana > 0

    def get_health(self):
        return self.cur_health

    def get_mana(self):
        return self.cur_mana

    def take_healing(self, healing_points):
        if self.is_alive():
            if self.cur_health + healing_points > self.max_health:
                self.cur_health = self.max_health
            else:
                self.cur_health += healing_points
            return True
        else:
            return False

    def take_mana(self, mana_points):
        if self.cur_mana + mana_points > self.max_mana:
            self.cur_mana = self.max_mana
            return self.cur_mana
        else:
            self.cur_mana += mana_points
            return self.cur_mana

    def equip(self, weapon):
        if type(weapon) == Weapon:
            self.weapons.append(weapon)
        elif type(weapon) == Spell:
            self.spells.append(weapon)

    def attack(self, **kwargs):
        if list(kwargs.keys())[0] == 'weapon':
            for weapon in self.weapons:
                if kwargs['weapon'] == weapon.name:
                    return weapon.damage
        elif list(kwargs.keys())[0] == 'magic':
            for spell in self.spells:
                if kwargs['spell'] == spell.name:
                    return spell.damage
        else:
            return self.damage

    def take_damage(self, damage_points):
        if self.cur_health - damage_points < 0:
            self.cur_health = 0
        else:
            self.cur_health -= damage_points
