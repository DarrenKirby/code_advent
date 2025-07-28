from collections import deque

with open("input/day18.txt", 'r') as f:
    lines = f.read().splitlines()

byte_positions = [tuple(map(int, s.split(','))) for s in lines]

gridmap = {(x, y): '.'
           for x in range(71)
           for y in range(71)}

for idx in range(1024):
    x, y = byte_positions[idx]
    gridmap[(x, y)] = 'X'


def bfs(grid, start=(0, 0), goal=(70, 70)) -> int:
    queue = deque([(start, 0)])  # (position, distance)
    visited = {start}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 4-way

    while queue:
        (x, y), dist = queue.popleft()
        if (x, y) == goal:
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            next_pos = (nx, ny)

            if next_pos in grid and grid[next_pos] == '.' and next_pos not in visited:
                visited.add(next_pos)
                queue.append((next_pos, dist + 1))

    return -1  # No path found


# part 1
print(bfs(gridmap))

# part 2
n = 1025
while True:
    x, y = byte_positions[n]
    gridmap[(x, y)] = 'X'
    if bfs(gridmap) == -1:
        print(f"{x},{y}")
        break
    n += 1
