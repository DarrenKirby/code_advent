import itertools

with open("input7.txt", 'r') as f:
    lines = f.read().splitlines()

lines = [line.split() for line in lines]

def generate_expressions(numbers):
    operators = ['+', '*']
    n = len(numbers) - 1
    operator_combinations = itertools.product(operators, repeat=n)
    expressions = []

    for combination in operator_combinations:
        expr = numbers[0]
        for i, operator in enumerate(combination):
            expr = f"({expr} {operator} {numbers[i + 1]})"
        expressions.append(expr)

    return expressions

test_values = []
for line in lines:
    good = False
    line[0] = int(line[0][:-1])
    results = generate_expressions(line[1:])
    for expr in results:
        #print(f"{expr}={eval(expr)} test value: {line[0]}")
        if eval(expr) == line[0]:
            good = True
    if good:
        test_values.append(line[0])

print(sum(test_values))
