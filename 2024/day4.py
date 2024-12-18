import numpy as np

with open("input4.txt", 'r') as f:
    lines = f.read().splitlines()

grid = np.array(list(map(list, lines)))

def find_xmases(i, j):
    nxmas = 0
    dirs = {
        "N": [(i-1,j),(i-2,j),(i-3,j)],
        "NE": [(i-1,j+1),(i-2,j+2),(i-3,j+3)],
        "E": [(i,j+1),(i,j+2),(i,j+3)],
        "SE": [(i+1,j+1),(i+2,j+2),(i+3,j+3)],
        "S": [(i+1,j),(i+2,j),(i+3,j)],
        "SW": [(i+1,j-1),(i+2,j-2),(i+3,j-3)],
        "W": [(i,j-1),(i,j-2),(i,j-3)],
        "NW": [(i-1,j-1),(i-2,j-2),(i-3,j-3)]
    }
    for direction, indices in dirs.items():
        if all(0 <= x < grid.shape[0] and 0 <= y < grid.shape[1] for x, y in indices):
            if grid[indices[0]] == 'M' and grid[indices[1]] == 'A' and grid[indices[2]] == 'S':
                nxmas += 1
    return nxmas

n = 0
for i in range(0, grid.shape[0]):
    for j in range(0, grid.shape[1]):
        if grid[i,j] == 'X':
            n += find_xmases(i,j)
print(n)
