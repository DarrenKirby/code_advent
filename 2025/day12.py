import numpy as np

lines = [l.strip() for l in open('input/day12.txt').readlines()]

shapes = {}
raw_shapes = lines[:30]
raw_regions = lines[30:]

ptr = 1
for i in range(6):
    shapes[i] = np.array([[1 if c == '#' else 0 for c in row] for row in raw_shapes[ptr:ptr + 3]])
    ptr += 5

regions = []
for r in raw_regions:
    gridsize, rest = r.split(": ")
    x, y = gridsize.split("x")
    t = int(x), int(y)
    l = [int(n) for n in rest.split(" ")]
    regions.append([t, l])

fits = 0
for r in regions:
    grid_size = r[0][0] * r[0][1]
    fill_size = sum(r[1]) * 7
    if fill_size <= grid_size:
        fits += 1

print(fits)
