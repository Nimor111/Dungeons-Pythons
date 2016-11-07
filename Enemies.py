class Enemy:
    def __init__(self, health=100, mana=100, damage=20):
        self.max_health = self.cur_health = health
        self.max_mana = self.cur_mana = mana
        self.damage = damage

    def is_alive(self):
        return self.cur_healh > 0

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

    def take_mana(mana_points):
        if self.cur_mana + mana_points > self.max_mana:
            self.cur_mana = self.max_mana
            return self.cur_mana
        else:
            self.cur_mana += cur_mana
            return self.cur_mana

    def attack(by):
        if attack == "weapon":

        else:

    def take_damage(self, damage_points):
        if self.cur_health - damage_points < 0:
            self.cur_health = 0
        else:
            self.cur_health -= damage_points
