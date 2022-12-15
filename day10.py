with open("day10test.txt", "r") as f:
    text = f.read()

lines = text.split("\n")



class Computer:
    def __init__(self):
        self.x:int = 1
        self.t: int = 0
        self.instructions: dict[int, int] = {}
        self.history = {}
        self.signal_strength = []

    def add_instruction(self, x):
        self.instructions[self.t+2]  = x

    def execute_instructions(self):
        try:
            self.x += self.instructions.pop(self.t)
        except KeyError:
            return

    def cycle(self, instruction):
        self.report_signal_strength()
        x = self.parse_instruction(instruction)
        if x is not None:
            self.add_instruction(x)
        self.execute_instructions()
        self.t += 1

    def parse_instruction(self, instruction):
        if instruction[:4] =='noop':
            return None
        return int(instruction[4:])

    def report_signal_strength(self, length = 20):
        self.history[self.t] = self.x
        if (self.t + 1) % length == 0:
            self.signal_strength.append(self.x )
comp = Computer()
for i, instruction in enumerate(lines):
    comp.cycle(instruction)
comp.cycle('noop')
comp.cycle('noop')
comp.cycle('noop')

print(comp.history.values())
print((comp.signal_strength))
