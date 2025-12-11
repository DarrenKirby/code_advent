lines = [l.strip() for l in open('input/day11.txt').readlines()]
paths = {}
for line in lines:
    key, val = line.split(": ")
    paths[key] = [i for i in val.split(" ")]


def count_paths(graph, start, end, memo=None):
    if memo is None:
        memo = {}

    if start == end:
        return 1
    if start in memo:
        return memo[start]

    total = 0
    for nxt in graph.get(start, []):
        total += count_paths(graph, nxt, end, memo)

    memo[start] = total
    return total


def count_paths_via_two(graph, start, end, foo, bar):
    # order: entry → foo → bar → exit
    order1 = (
            count_paths(graph, start, foo, {}) *
            count_paths(graph, foo, bar, {}) *
            count_paths(graph, bar, end, {})
    )

    # order: entry → bar → foo → exit
    order2 = (
            count_paths(graph, start, bar, {}) *
            count_paths(graph, bar, foo, {}) *
            count_paths(graph, foo, end, {})
    )

    return order1 + order2


# Part 1
print(count_paths(paths, "you", "out"))
# Part 2
print(count_paths_via_two(paths, "svr", "out", "dac", "fft"))
