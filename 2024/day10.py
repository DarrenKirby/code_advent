with open("input10.txt", 'r') as f:
    lines = f.read().splitlines()

# Other folks seem to like using a dict to represent the grid,
# so I thought I would give it a try.
grid = { ( x, y ): int(char)
         for y, row in enumerate(lines)
         for x, char in enumerate( row.strip( '\n' ) ) }

# Don't actually use these, but may be useful for other puzzles
xmin, *_, xmax = sorted( { x for x, y in grid.keys() } )
ymin, *_, ymax = sorted( { y for x, y in grid.keys() } )

def score_trail(grid, coords, part1=True):
    score = 0
    visited = set()
    queue = [coords]

    while queue:
        cur = queue.pop()
        if part1:
            if cur in visited:
                continue
        visited.add(cur)
        if (val := grid[cur]) == 9:
            score += 1
            continue
        queue.extend(
            n for n in [(cur[0]-1, cur[1]), # N
                        (cur[0], cur[1]+1), # E
                        (cur[0]+1, cur[1]), # S
                        (cur[0], cur[1]-1)] # W
            if grid.get(n) == val + 1
        )
    return score

print(sum(
    score_trail(grid, trailhead)
    for trailhead, v in grid.items()
    if v == 0
))
print(sum(
    score_trail(grid, trailhead, part1=False)
    for trailhead, v in grid.items()
    if v == 0
))
