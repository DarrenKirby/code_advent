data = []
with open("input/day1.txt", "r") as f:
    for line in f:
        data.append((line[:1], int(line[1:].strip())))

pointer = 50
n_exact_zeros = 0
n_zero_crosses = 0

for direction, magnitude in data:
    if direction == "R":
        k0 = (100 - pointer) % 100
        pointer = (pointer + magnitude) % 100
    else:
        k0 = pointer % 100
        pointer = (pointer - magnitude) % 100

    if k0 == 0:
        k0 = 100
    if magnitude >= k0:
        n_zero_crosses += 1 + (magnitude - k0) // 100
    if pointer == 0:
        n_exact_zeros += 1

print(f"part1: {n_exact_zeros} part2: {n_zero_crosses}")
