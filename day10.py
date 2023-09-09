from aocd import data

# with open("test.txt", "r") as f:
#     data = f.read()

data = data.strip().split("\n")


class CommSystem:
    opcode2cycle_len = {"addx": 2, "noop": 1}

    def __init__(self):
        self.reg_X = 1
        self.cycle = 1
        self.beam_pos = 0
        self.buffer = ""

    def addx(self, v):
        self.reg_X += v

    def noop(self, arg):
        pass

    def clock_tick(self):
        if self.beam_pos in range(self.reg_X - 1, self.reg_X + 2):
            self.buffer += "#"
        else:
            self.buffer += "."

        if self.beam_pos % 40 == 39:
            self.buffer += "\n"
            self.beam_pos = 0
        else:
            self.beam_pos += 1
        self.cycle += 1

    def run_op(self, opcode, arg):
        opcode2op = {"addx": self.addx, "noop": self.noop}
        opcode2op[opcode](arg)


watched_cycles = [20, 60, 100, 140, 180, 220]
sig_str_rec = []

cs = CommSystem()

for row in data:
    inst = row.split(" ")
    opcode = inst[0]
    arg = int(inst[1]) if len(inst) > 1 else 0

    for _ in range(cs.opcode2cycle_len[opcode]):
        if cs.cycle in watched_cycles:
            sig_str_rec.append(cs.cycle * cs.reg_X)
        cs.clock_tick()

    cs.run_op(opcode, arg)


solution_a = sum(sig_str_rec)
print(f"{solution_a = }")


cs = CommSystem()

for row in data:
    inst = row.split(" ")
    opcode = inst[0]
    arg = int(inst[1]) if len(inst) > 1 else 0

    for _ in range(cs.opcode2cycle_len[opcode]):
        cs.clock_tick()
    cs.run_op(opcode, arg)

print(cs.buffer)
