class Weapon:

    def __init__(self, name="The Axe of Despair", damage=20):
        self.name = name
        self.damage = damage

    def __str__(self):
        return "Name: {}, Damage: {}".format(self.name, self.damage)

    def __repr__(self):
        return self.__str__()
