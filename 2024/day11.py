import time
from functools import lru_cache

with open("input/day11.txt", 'r') as f:
    lines = f.read().splitlines()

stones_l = [int(s) for s in lines[0].split()]


# Part 1
def permute_stones(stones):
    s = []
    for stone in stones:
        if stone == 0:
            s.append(1)
        elif len(str(stone)) % 2 == 0:
            stone = str(stone)
            s.append(int(stone[0:len(stone) // 2]))
            s.append(int(stone[len(stone) // 2:]))
        else:
            s.append(stone * 2024)
    return s


for _ in range(25):
    stones_l = permute_stones(stones_l)

print(len(stones_l))

# Part 2
# Too much growth to brute-force
start = time.time()


# Don't really need the cache; dict is fast enough
# but it does basically halve the runtime. Executes
# for ~2s without ~1s with the cache at n=500 iterations.
@lru_cache(maxsize=None)
def permute_stone(s):
    if s == 0:
        return [1]
    elif len(str(s)) % 2 == 0:
        s = str(s)
        l, r = int(s[0:len(s) // 2]), int(s[len(s) // 2:])
        return [l, r]
    else:
        return [s * 2024]


stones_l = [int(s) for s in lines[0].split()]
stone_counter = dict((n, 1) for n in stones_l)
for _ in range(75):
    tmp_stone_counter = dict()
    for num, n in stone_counter.items():
        for n_new in permute_stone(num):
            if n_new in tmp_stone_counter:
                tmp_stone_counter[n_new] += n
            else:
                tmp_stone_counter[n_new] = n
    stone_counter = tmp_stone_counter

result = sum(n for n in stone_counter.values())
print(result)
end = time.time()
print(end - start)
