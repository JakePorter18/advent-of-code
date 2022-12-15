from time import sleep


with open("day10.txt", "r") as f:
    text = f.read()

lines = text.split("\n")



class Computer:
    def __init__(self, instruction_set):
        self.x = 1
        self.t = 0
        self.instruction_set = instruction_set
        self.history = []
        self.instructions = []
        self.strengths = []

    def cycle(self):
        comp.t += 1
        self.save_state()
        if len(self.instructions) == 0:
            self.add_instruction()

        for instruction in self.instructions:
            if instruction.execute_in == 0:
                self.x += instruction.movement
                instruction.executed = True
            instruction.execute_in -= 1

        self.instructions = [i for i in self.instructions if instruction.executed == False]

    def add_instruction(self):
        try:
            self.instructions.append(Instruction(self.instruction_set.pop(0)))
        except IndexError:
            return

    def save_state(self, length = 40, rem = 20):
        strength = self.x * self.t

        self.history.append(self.x)
        if self.t % length == rem:
            self.strengths.append(strength)

    def is_active(self):
        if len(self.instruction_set) + len(self.instructions) != 0:
            return True
        return False


class Instruction:
    def __init__(self, instruction_text):
        self.executed = False
        if instruction_text[:4] =='noop':
            self.movement = 0
            self.execute_in = 0
        else:
            self.movement = int(instruction_text[4:])
            self.execute_in = 1

comp = Computer(lines)
while comp.is_active():
    comp.cycle()

for i, val in enumerate(comp.history):
    sprite_pos = [val, val+1, val-1]
    cursor = ((i) % 40)
    if cursor in sprite_pos:
        print("■", end='', flush=True)
    else:
        print(" ", end='', flush=True)

    if cursor == 39:
        print("", flush=True)
    sleep(0.01)