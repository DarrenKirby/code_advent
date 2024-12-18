with open("input5.txt", 'r') as f:
    data = f.read().splitlines()

ordering = [line.split("|") for line in data if line.find("|") > 0]
updates = [line.split(",") for line in data if line.find(",") > 0]

not_in_order = []
in_order = updates.copy()
for lst in updates[:]:
    for pair in ordering:
        if pair[0] in lst and pair[1] in lst:
            if lst.index(pair[0]) > lst.index(pair[1]):
                in_order.remove(lst)
                not_in_order.append(lst)
                break

to_sum = []
for l in in_order:
    to_sum.append(int(l[len(l) // 2]))
print(sum(to_sum))

def topological_sort(graph: dict) -> list:
    visited = set()
    stack = []

    def dfs(node, path):
        nonlocal visited, stack

        if node not in visited:
            visited.add(node)
            path.append(node)
            for neighbor in graph[node]:
                dfs(neighbor, path)
            path.pop()
            stack.append(node)

    for outer_node in graph:
        if outer_node not in visited:
            dfs(outer_node, [])

    return stack

# Part 2
ordered = []
for lst in not_in_order:
    graph = {}
    for pair in ordering:
        if pair[0] in lst and pair[1] in lst:
            graph.setdefault(pair[0], []).append(pair[1])
    for v in lst:
        if v not in graph:
            graph[v] = []
    ordered.append(topological_sort(graph))

to_sum = []
for l in ordered:
    to_sum.append(int(l[len(l) // 2]))
print(sum(to_sum))
