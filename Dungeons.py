MOVEMENT = {"right": (0, 1),
            "left": (0, -1),
            "up": (-1, 0),
            "down": (1, 0)
            }


class Dungeon:
    def __init__(self, file_path):
        with open(file_path, "r") as f:
            self.map = f.read().splitlines()

    def print_map(self):
        for line in self.map_list:
            print("".join(line))

    def spawn(self):
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

    def validate(self, direction):
        return MOVEMENT[direction][0] + self.j >= 0 and\
               MOVEMENT[direction][0] + self.j < len(self.map) and\
               MOVEMENT[direction][1] + self.i >= 0 and\
               MOVEMENT[direction][1] + self.i < len(self.map[self.j]) and\
               self.map_list[MOVEMENT[direction][0] + self.i][MOVEMENT[direction][1] + self.j] == '.' or \
               self.map_list[MOVEMENT[direction][0] + self.i][MOVEMENT[direction][1] + self.j] == 'T'

    def move_hero(self, direction):
        if self.validate(direction):
            self.map_list[self.i][self.j] = '.'
            self.i += MOVEMENT[direction][0]
            self.j += MOVEMENT[direction][1]
            self.map_list[self.i][self.j] = 'H'
            return True
        else:
            return False
