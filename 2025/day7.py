with open("input/day7.txt", "r") as f:
    lines = f.read().splitlines()

xmax = len(lines)
ymax = len(lines[0])

grid: dict[tuple[int, int], str] = \
    {(x, y): char
     for x, row in enumerate(lines)
     for y, char in enumerate(row.strip('\n'))}


def process_part1(r: int, c: int) -> int:
    if grid[r, c] == '|':
        try:
            if grid[r + 1, c] == '.':
                grid[r + 1, c] = '|'
                return 0
            elif grid[r + 1, c] == '^':
                grid[r + 1, c + 1] = '|'
                grid[r + 1, c - 1] = '|'
                return 1
        except KeyError:
            return 0
    return 0


grid[1, xmax // 2 - 1] = '|'
splits = 0
for row in range(xmax):
    for col in range(ymax):
        splits += process_part1(row, col)

# part 1
print(splits)


def process_part2(r: int, c: int) -> None:
    if grid[r, c] == '^' and type(grid[r - 1, c]) == int:
        digit = grid[r - 1, c]
        try:
            if type(grid[r, c - 1]) == int:
                digit2 = grid[r, c - 1]
                grid[r, c - 1] = digit + digit2
            else:
                grid[r, c - 1] = digit
            if type(grid[r, c + 1]) == int:
                digit3 = grid[r, c + 1]
                grid[r, c + 1] = digit + digit3
            else:
                grid[r, c + 1] = digit
        except KeyError:
            pass


def drop_row(r: int) -> None:
    for i in range(ymax):
        if type(grid[r, i]) == int:
            try:
                if grid[row + 1, i] != '^':
                    grid[row + 1, i] = grid[r, i]
            except KeyError:
                pass


# Not used, other than for debugging
def p_grid() -> None:
    for r in range(xmax):
        for c in range(ymax):
            print(f" {grid[r, c]} ", end='')
        print()
    print()


grid: dict[tuple[int, int], str | int] = \
    {(x, y): char
     for x, row in enumerate(lines)
     for y, char in enumerate(row.strip('\n'))}

grid[1, xmax // 2 - 1] = 1
for row in range(xmax):
    for col in range(ymax):
        process_part2(row, col)
    drop_row(row)

total = 0
for pos in range(ymax):
    if isinstance(grid[xmax - 1, pos], int):
        n = int(grid[xmax - 1, pos])
        total += n

#part 2
print(total)
