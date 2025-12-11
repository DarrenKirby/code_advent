from itertools import combinations
from math import dist

junctions = [tuple(int(n) for n in l.split(",")) for l in open("input/day8.txt").readlines()]
circuits = {b: {b} for b in junctions}


def get_distance(x: tuple[tuple[int, int, int], tuple[int, int, int]]):
    return dist(x[0], x[1])


combos = tuple(combinations(circuits, 2))
pairs = sorted(combos, key=get_distance)

for i, (box1, box2) in enumerate(pairs):
    cir1, cir2 = None, None
    for c in circuits:
        if box1 in circuits[c]: cir1 = c
        if box2 in circuits[c]: cir2 = c

    if cir1 != cir2:
        circuits[cir1] |= circuits[cir2]
        del circuits[cir2]

    if i + 1 == 1000:
        n = sorted(len(circuits[b]) for b in circuits)
        print(n[-3] * n[-2] * n[-1])

    if len(circuits) == 1:
        print(box1[0] * box2[0])
        break
