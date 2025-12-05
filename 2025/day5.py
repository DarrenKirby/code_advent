with open("input/day5.txt", "r") as f:
    lines = f.read().splitlines()

id_ranges = []
ids = []
split_idx = lines.index("")
for i in lines[:split_idx]:
    id_ranges.append(tuple(i.split("-")))
for j in lines[split_idx + 1:]:
    ids.append(int(j))

id_r = [range(int(lo), int(hi) + 1) for lo, hi in id_ranges]

good = set()
for ingredient in ids:
    for rge in id_r:
        if ingredient in rge:
            good.add(ingredient)

# part 1
print(len(good))

def count_unique_values(ranges):
    pairs = [(r.start, r.stop) for r in ranges]
    pairs.sort()

    merged = []
    cur_start, cur_end = pairs[0]

    for s, e in pairs[1:]:
        if s > cur_end:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = s, e
        else:
            cur_end = max(cur_end, e)

    merged.append((cur_start, cur_end))

    return sum(e - s for s, e in merged)

#part 2
print(count_unique_values(id_r))
