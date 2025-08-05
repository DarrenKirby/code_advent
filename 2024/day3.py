import re

data = ""
with open("input/day3.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        data += line

valid_instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)", data)

# part 1
products1 = []
for mul in valid_instructions:
    try:
        nums = mul[4:-1]
        f1, f2 = nums.split(",")
        products1.append(int(f1) * int(f2))
    except ValueError:
        continue

print(sum(products1))

# part 2
products2 = []
process = True
for inst in valid_instructions:
    if inst == "do()":
        process = True
    elif inst == "don't()":
        process = False
    elif process:
        nums = inst[4:-1]
        f1, f2 = nums.split(",")
        products2.append(int(f1) * int(f2))

print(sum(products2))
