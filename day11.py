from aocd import data
from math import lcm
from copy import deepcopy

# with open("test.txt", "r") as f:
#     data = f.read()

data = data.split("\n")


monkey_items_init = []
monkey_ops = []
monkey_test_params = []
monkey_if_true = []
monkey_if_false = []
monkey_business = []


def make_op(opcode: str, operand: int = None) -> callable:
    if opcode == "*" and not operand:
        return lambda x: x * x
    elif opcode == "+" and not operand:
        return lambda x: x + x
    elif opcode == "*":
        return lambda x: x * operand
    elif opcode == "+":
        return lambda x: x + operand


for line_raw in data:
    line = line_raw.strip()
    if line.startswith("Monkey "):
        # idx = int(line.strip(":").split(" ")[1])
        monkey_business.append(0)
    if line.startswith("Starting items: "):
        monkey_items_init.append([int(n) for n in line[16:].split(", ")])
    if line.startswith("Operation: "):
        inst = line[11:].split(" ")
        op = inst[-2]
        val = inst[-1]
        monkey_ops.append(make_op(op, None if val == "old" else int(val)))
    if line.startswith("Test: "):
        monkey_test_params.append(int(line.split(" ")[-1]))
    if line.startswith("If true: "):
        monkey_if_true.append(int(line.split(" ")[-1]))
    if line.startswith("If false: "):
        monkey_if_false.append(int(line.split(" ")[-1]))

# Done parsing. Now solve the problem.


def main_loop(num_rounds, part_b=False):
    modulus = lcm(*monkey_test_params)
    monkey_items = deepcopy(monkey_items_init)
    for _ in range(num_rounds):
        for monkey_idx, items in enumerate(monkey_items):
            for _ in range(len(items)):
                monkey_business[monkey_idx] += 1
                item = items.pop(0)
                if part_b:
                    item = monkey_ops[monkey_idx](item) % modulus
                else:
                    item = monkey_ops[monkey_idx](item) // 3
                if item % monkey_test_params[monkey_idx] == 0:
                    monkey_items[monkey_if_true[monkey_idx]].append(item)
                else:
                    monkey_items[monkey_if_false[monkey_idx]].append(item)


main_loop(20)
solution_a = sorted(monkey_business)[-2] * sorted(monkey_business)[-1]
print(f"{solution_a = }")

# Reset for part (b)

monkey_business = [0 for _ in monkey_business]

main_loop(10_000, part_b=True)
solution_b = sorted(monkey_business)[-2] * sorted(monkey_business)[-1]
print(f"{solution_b = }")
