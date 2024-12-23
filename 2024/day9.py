with open("input9.txt", 'r') as f:
    lines = f.readlines()
# Input is one long string with \n
line = lines[0][:-1]

# Part 1
def make_disk_map(line):
    disk_map = []
    file_id = 0
    for idx, val in enumerate(line):
        val = int(val)
        # val is file block
        if idx % 2 == 0:
            disk_map += [file_id] * val
            file_id += 1
        # val is free space
        else:
            disk_map += [-1] * val
    return disk_map

disk_map = make_disk_map(line)

free_space = [i for i, v in enumerate(disk_map) if v == -1]

for i in free_space:
    while disk_map[-1] == -1:
        disk_map.pop()
    if len(disk_map) <= i:
        break
    disk_map[i] = disk_map.pop()

prod = []
for idx, val in enumerate(disk_map):
    prod.append(idx * val)

print(sum(prod))

# Part 2 - big thanks to HyperNuetrino for showing me
# the way. My original part 2 solution was huge and
# ugly and produced the wrong answer
file_id = 0
pos = 0

files = {}
free = []

for idx, val in enumerate(line):
    val = int(val)
    if idx % 2 == 0:
        files[file_id] = (pos, val)
        file_id += 1
    else:
        free.append((pos, val))
    pos += val

while file_id > 0:
    file_id -= 1
    pos, size = files[file_id]
    for i, (start, length) in enumerate(free):
        if start >= pos:
            free = free[:i]
            break
        if size <= length:
            files[file_id] = (start, size)
            if size == length:
                free.pop(i)
            else:
                free[i] = (start + size, length - size)
            break
total = 0
for file_id, (pos, size) in files.items():
    for x in range(pos, pos + size):
        total += file_id * x

print(total)
