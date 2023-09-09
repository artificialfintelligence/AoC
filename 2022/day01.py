from aocd import data, submit

data = data.split("\n")
data_list = [elf.split("\n") for elf in data.split("\n\n")]
foods_per_elf = [[int(food) for food in foods] for foods in data_list]
total_cals_per_elf = [sum(cals) for cals in foods_per_elf]
highest_total_calories = max(total_cals_per_elf)
