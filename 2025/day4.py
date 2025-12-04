    with open("input/day4.txt", "r") as f:
        lines = f.read().splitlines()

    xmax = len(lines)
    ymax = len(lines[0])

    grid = {(x, y): char
            for y, row in enumerate(lines)
            for x, char in enumerate(row.strip('\n'))}

    good_spots = set()

    def check_spot(x, y, remove=False) -> bool:
        if grid[(x, y)] == '.':
            return False
        bales = 0
        for spot in [(x, y + 1), (x, y - 1), (x + 1, y + 1), (x + 1, y - 1),
                     (x - 1, y + 1), (x - 1, y - 1), (x - 1, y), (x + 1, y)]:
            try:
                if grid[spot] == '@':
                    bales += 1
            except KeyError:
                pass
        if bales < 4:
            good_spots.add(spot)
            if remove:
                grid[x, y] = '.'
            return True
        return False

    for r in range(xmax):
        for c in range(ymax):
            check_spot(r, c)

    # part 1
    print(len(good_spots))

    num_removed = 0
    while True:
        removed_this_loop = 0
        for r in range(xmax):
            for c in range(ymax):
                if check_spot(r, c, True):
                    removed_this_loop += 1
                    num_removed += 1
        if removed_this_loop == 0:
            break

    # Part 2
    print(num_removed)
