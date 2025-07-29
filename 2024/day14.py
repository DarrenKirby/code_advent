with open("input/day14.txt", 'r') as f:
    lines = f.read().splitlines()

w = 101
h = 103

bots = []

for line in lines:
    pos, vel = line.split()
    pos = pos.replace("p=", "")
    vel = vel.replace("v=", "")
    x, y = pos.split(",")
    dx, dy = vel.split(",")
    bots.append((int(x), int(y), int(dx), int(dy)))

result = []
for bot in bots:
    r2 = (bot[0] + bot[2] * 100) % w
    c2 = (bot[1] + bot[3] * 100) % h
    result.append((r2, c2))

q1 = q2 = q3 = q4 = 0

vert_m = (h - 1) // 2
hort_m = (w - 1) // 2

for x, y in result:
    if x == hort_m or y == vert_m:
        continue
    if x < hort_m:
        if y < vert_m:
            q1 += 1
        else:
            q2 += 1
    else:
        if y < vert_m:
            q3 += 1
        else:
            q4 += 1

# part 1
print(q1 * q2 * q3 * q4)
# part 2
result = []
botx = set()
for i in range(100000):
    botx.clear()  # = set()
    for bot in bots:
        r2 = (bot[0] + bot[2] * i) % w
        c2 = (bot[1] + bot[3] * i) % h
        result.append((r2, c2))
        botx.add((r2, c2))
    if len(botx) == 500:
        print(f"no overlaps on iteration {i}")
        break
# print the tree
s = "\n".join("".join(" " if (x, y) not in botx else "#" for x in range(103)) for y in range(101))
print(s)
