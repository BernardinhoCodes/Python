


class Player:
    pass

class Field:
    @staticmethod
    def gen_random():
        pass

class Map:
    def __init__(self, width, height):
        self.state = []
        self.x = 0
        self.y = 0
        for i in range(width):
            fields = []
            for j in range(height):
                fields.append(Field.gen_random())
            self.state.append(fields)

    def print_state(self):
        self.state[self.x][self.y].print_state()

    def sprint(self):
        if self.x == len()






def sprint(p, m):
    m.sprint()

def right(p, m):
    m.right()

def left(p, m):
    m.left()

def backwards(p, m):
    m.backwards()

def save(p, m):
    pass

def load(p, m):
    pass

def quit_exit(p, m):
    print("Aiiighht...you don't want it bad enough...come back")
    exit(0)

def help_game(p, m):
    print(Commands.keys())

Commands = {
    'help': help_game,
    'quit': quit_exit,
#---------------------------

    'shoot': shoot,
    'pass': passing,

#--------------------------
    'sprint': sprint,
    'chop-right': right,
    'chop-left': left,
    'turn-back': backwards,

#--------------------------
    'save': save,
    'load': load,

}




if __name__ == '__main__':
    p = Player(name)
    map = Map()
    print("(type 'help' to list the different command)\n")

    while True:
        command = input(">").lower().split(" ") #pickup axe
        if command[0] in Commands:
                Commands[command[0]](p, map)
        else:
            print("You leavin the pitch...Stay and play")
        map.print_state()