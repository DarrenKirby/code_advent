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
with open("output.txt", "w") as f:
    np.savetxt(f, grid, fmt='%s', delimiter='', newline='\n')
