import re
with open("input3.txt", "r") as f:
    lines = f.readlines()

# part 1
products = []
regex = r"mul\(\d{1,3},\d{1,3}\)"

for line in lines:
    matches = re.findall(regex, line)
    for match in matches:
        #print(match)
        nums = match[4:-1]
        f1, f2 = nums.split(",")
        products.append(int(f1) * int(f2))

print(sum(products))

# part 2

data = ""
with open("input3.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        data += line


valid_instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)", data)
products1 = []
for mul in valid_instructions:
    try:
        nums = mul[4:-1]
        f1, f2 = nums.split(",")
        products1.append(int(f1) * int(f2))
    except ValueError:
        continue

print(sum(products1))

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
