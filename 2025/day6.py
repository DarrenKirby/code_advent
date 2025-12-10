from math import prod
from itertools import zip_longest

with open("input/day6.txt", "r") as f:
    lines = f.read().splitlines()

key = [line.split() for line in lines]
ops = list(zip(*key))

grand_total = 0
for p in ops:
    if p[-1] == '*':
        grand_total += prod([int(t) for t in p[:-1]])
    else:
        grand_total += sum([int(t) for t in p[:-1]])

# part 1
print(grand_total)

with open("input/day6.txt") as f:
    rows = f.read().splitlines()

cols = list(zip_longest(*rows, fillvalue=' '))

grand_total = 0
idx = 0
while idx < len(cols):
    row = cols[idx]
    # operator is always last element of the tuple
    op = row[-1]

    operands = []
    # read operand rows until a blank tuple
    while idx < len(cols) and any(c != ' ' for c in cols[idx]):
        tup = cols[idx]
        # everything except the last column is a potential digit
        digit_part = ''.join(c for c in tup[:-1] if c.isdigit())
        if digit_part:
            operands.append(int(digit_part))
        idx += 1

    # Now we’re on the blank separator row — skip it
    idx += 1
    # Apply the operation
    if op == '+':
        grand_total += sum(operands)
    else:
        grand_total += prod(operands)

print(grand_total)
