import numpy as np

with open("input6.txt", 'r') as f:
    lines = f.read().splitlines()

grid = np.array(list(map(list, lines)))
# start position indices
idx = np.where(grid == "^")
i, j = idx[0].item(), idx[1].item()
visited = set()
index = (i,j)
visited.add(index)
move = [(-1,0), (0,1), (1,0), (0,-1)]
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
with open("output.txt", "w") as f:
    np.savetxt(f, grid, fmt='%s', delimiter='', newline='\n')

# Part 2
rows, cols = grid.shape
# Fresh grid for cycle detection
cyclic_grid = np.array(list(map(list, lines)))

for r in range(rows):
    for c in range(cols):
        if cyclic_grid[r, c] == "^":
            index = (r,c)

def is_cycle(grid, index):
    r = index[0]
    c = index[1]
    dr = -1
    dc = 0
    visited = set()
    while True:
        visited.add((r, c, dr, dc))
        if r + dr < 0 or r + dr >= rows or c + dc < 0 or c + dc >= cols:
            # We've left the map. No cycle
            return False
        if grid[r + dr, c + dc] == '#':
            dc, dr = -dr, dc
        else:
            r += dr
            c += dc
        if (r, c, dr, dc) in visited:
            # Same location and dirrection. It's a cycle
            return True

# Find trodden spots to place obstacles
cycles = 0
for nr in range(rows):
    for nc in range(cols):
        # Use our previously marked up grid
        if grid[nr,nc] == "X":
            cyclic_grid[nr,nc] = '#'
            if is_cycle(cyclic_grid, index):
                cycles += 1
            # Remove the obstacle
            cyclic_grid[nr, nc] = '.'

print(cycles)
