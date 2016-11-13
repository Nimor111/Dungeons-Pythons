from random import randint
from Hero import *
# from Fights import *
from Enemies import *

MOVEMENT = {"right": (0, 1),
            "left": (0, -1),
            "up": (-1, 0),
            "down": (1, 0)
            }


class Dungeon:
    def __init__(self, map_file, treasure_file):
        with open(map_file, "r") as f:
            self.map = f.read().splitlines()
        with open(treasure_file, "r") as f:
            self.treasure_list = f.read().split(',')

    def print_map(self):
        for line in self.map_list:
            print("".join(line))

    def spawn(self, hero):
        self.hero = hero
        line_list = []
        new_line = ''
        for index in range(len(self.map)):
            if 'S' in self.map[index]:
                line_list = self.map[index].split('S')
                new_line += line_list[0]
                self.j = len(line_list[0])
                self.i = index
                new_line += 'H'
                new_line += line_list[1]
                del self.map[index]
                self.map.insert(index, new_line)
        self.map_list = [list(i) for i in self.map]
        return self.map

    def pick_treasure(self):
        return self.treasure_list[randint(0, len(self.treasure_list) - 1)]

    def validate(self, direction):
        # print("----------------------------------------")
        # print(MOVEMENT[direction][0] + self.i >= 0)
        # print(MOVEMENT[direction][0] + self.i < len(self.map))
        # print(MOVEMENT[direction][1] + self.j)
        # print(MOVEMENT[direction][1] + self.j < len(self.map[self.i - 1]))
        return MOVEMENT[direction][0] + self.i >= 0 and\
               MOVEMENT[direction][0] + self.i < len(self.map) and\
               MOVEMENT[direction][1] + self.j >= 0 and\
               MOVEMENT[direction][1] + self.j < len(self.map[self.i - 1]) and\
               (self.map_list[MOVEMENT[direction][0] + self.i][MOVEMENT[direction][1] + self.j] == '.' or
                self.map_list[MOVEMENT[direction][0] + self.i][MOVEMENT[direction][1] + self.j] == 'T' or
                self.map_list[MOVEMENT[direction][0] + self.i][MOVEMENT[direction][1] + self.j] == 'E')

    def move_hero(self, direction):
        print(self.validate(direction))
        if self.validate(direction):
            self.map_list[self.i][self.j] = '.'
            self.i += MOVEMENT[direction][0]
            self.j += MOVEMENT[direction][1]
            print(str(self.i) + ' ' + str(self.j))
            if self.map_list[self.i][self.j] == 'T':
                pot = self.pick_treasure()
                print("Found " + pot + "potion.")
                if pot == "health":
                    self.hero.take_healing(10)
                    # Should take health value from the file
                else:
                    # Should take health value from the file
                    self.hero.take_mana(10)
            elif self.map_list[self.i][self.j] == 'E':
                pass
            self.map_list[self.i][self.j] = 'H'
            return True
        else:
            return False
