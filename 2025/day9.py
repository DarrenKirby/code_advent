from itertools import combinations
from math import dist
from shapely import Polygon

coords = [tuple(int(n) for n in l.split(",")) for l in open("input/day9.txt").readlines()]


def get_distance(x: tuple[tuple[int, int, int], tuple[int, int, int]]):
    return dist(x[0], x[1])


combos = tuple(combinations(coords, 2))
pairs = sorted(combos, key=get_distance)

areas = []
for (x1, y1), (x2, y2) in pairs:
    height = abs(x2 - x1) + 1
    width = abs(y2 - y1) + 1
    areas.append(height * width)

# Part 1
print(sorted(areas)[-1])

areas2 = []
bound_box = Polygon(coords)

for n1 in coords:
    for n2 in coords:
        min_x = min(n1[0], n2[0])
        min_y = min(n1[1], n2[1])
        max_x = max(n1[0], n2[0])
        max_y = max(n1[1], n2[1])
        this_poly = Polygon([(min_x, min_y), (max_x, min_y), (max_x, max_y), (min_x, max_y)])
        if bound_box.contains(this_poly):
            areas2.append((abs(n1[0] - n2[0]) + 1) * (abs(n1[1] - n2[1]) + 1))

# FIXME: Part 2 very slow, look into how to optimize
# Part 2
print(sorted(areas2)[-1])
