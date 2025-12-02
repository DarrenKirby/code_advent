import re

with open("input/day2.txt", "r") as f:
    lines = [line.strip() for line in f.readline().split(",")]

ranges = []
for rng in lines:
    lo, hi = rng.split("-")
    ranges.append((int(lo), int(hi)))

pat1 = re.compile(r'^((.+?)\2)$')
pat2 = re.compile(r'^(.+?)\1+$')
total1 = 0
total2 = 0

for r in ranges:
    for n in range(r[0], r[1] + 1):
        m1 = pat1.match(str(n))
        if m1:
            total1 += n
        m2 = pat2.match(str(n))
        if m2:
            total2 += n

print(f"part1: {total1} part2: {total2}")
