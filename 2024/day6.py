import numpy as np

with open("input/day6.txt", 'r') as f:
    lines = f.read().splitlines()

grid = np.array(list(map(list, lines)))
# start position indices
idx = np.where(grid == "^")
i, j = idx[0].item(), idx[1].item()
visited = set()
index = (i, j)
visited.add(index)
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
grid[index] = '*'
mov_i = 0

while 0 <= index[0] < grid.shape[0] and 0 <= index[1] < grid.shape[1]:
    n_index = (index[0] + move[mov_i][0], index[1] + move[mov_i][1])

    if not (0 <= n_index[0] < grid.shape[0] and 0 <= n_index[1] < grid.shape[1]):
        break

    if grid[n_index] == '#':
        mov_i = (mov_i + 1) % 4
    else:
        # Move forward, update visited positions
        index = n_index
        visited.add(index)
        grid[index] = 'X'

print(len(visited))

# Write to file with no spaces, one row per line
# This is not necessary to solve the challenge,
# it's just cool to see a visualization of the guard's walk
with open("input/day6_output.txt", "w") as f:
    np.savetxt(f, grid, fmt='%s', delimiter='', newline='\n')

# Part 2
rows, cols = grid.shape
# Fresh grid for cycle detection
cyclic_grid = np.array(list(map(list, lines)))

# Find origin
for y in range(rows):
    for x in range(cols):
        if cyclic_grid[y, x] == "^":
            index = (y, x)


def is_cycle(i_grid, i_index):
    r = i_index[0]
    c = i_index[1]
    dr = -1
    dc = 0
    i_visited = set()
    while True:
        # We must track dr/dc too, as visiting
        # a spot twice is not necessarily a cycle.
        i_visited.add((r, c, dr, dc))
        if r + dr < 0 or r + dr >= rows or c + dc < 0 or c + dc >= cols:
            # We've left the map. No cycle
            return False
        if i_grid[r + dr, c + dc] == '#':
            dc, dr = -dr, dc
        else:
            r += dr
            c += dc
        if (r, c, dr, dc) in i_visited:
            # Same location and direction. It's a cycle
            return True


# Find trodden spots to place obstacles
# using our previously marked up grid
cycles = 0
for nr in range(rows):
    for nc in range(cols):

        # Logic dictates only spots marked in the previous walk
        # make sense to place obstacles in. Using only these
        # dramatically reduces the search space
        if grid[nr, nc] == "X":
            cyclic_grid[nr, nc] = '#'
            if is_cycle(cyclic_grid, index):
                # Count if it's a cycle
                cycles += 1
            # Remove the obstacle and reset map
            cyclic_grid[nr, nc] = '.'

print(cycles)
