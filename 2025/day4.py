lines = [l for l in open("input/day4.txt").read().splitlines()]

xmax = len(lines)
ymax = len(lines[0])
good_spots = set()

grid: dict[tuple[int, int], str] = \
    {(x, y): char
     for y, row in enumerate(lines)
     for x, char in enumerate(row.strip('\n'))}


def check_spot(r: int, c: int, remove=False) -> bool:
    if grid[(r, c)] == '.':
        return False
    bales = 0
    for spot in [(r, c + 1), (r, c - 1), (r + 1, c + 1), (r + 1, c - 1),
                 (r - 1, c + 1), (r - 1, c - 1), (r - 1, c), (r + 1, c)]:
        try:
            if grid[spot] == '@':
                bales += 1
        except KeyError:
            pass
    if bales < 4:
        good_spots.add(spot)
        if remove:
            grid[r, c] = '.'
        return True
    return False


for row in range(xmax):
    for col in range(ymax):
        check_spot(row, col)

# part 1
print(len(good_spots))

num_removed = 0
while True:
    removed_this_loop = 0
    for row in range(xmax):
        for col in range(ymax):
            if check_spot(row, col, True):
                removed_this_loop += 1
                num_removed += 1
    if removed_this_loop == 0:
        break

# Part 2
print(num_removed)
