def pick_biggest(s: str, k: int) -> str:
    drop = len(s) - k
    out = []
    for c in s:
        while drop and out and out[-1] < c:
            out.pop()
            drop -= 1
        out.append(c)
    return ''.join(out[:k])

p1_joltage = 0
p2_joltage = 0

with open("input/day3.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

for bank in lines:
    p1_joltage += int(pick_biggest(bank, 2))
    p2_joltage += int(pick_biggest(bank, 12))

print(p1_joltage)
print(p2_joltage)

