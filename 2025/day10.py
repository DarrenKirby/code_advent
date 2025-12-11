from itertools import combinations
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

lines = [l.strip().split(' ') for l in open('input/day10.txt').readlines()]


class Machine:
    def __init__(self, data) -> None:
        self.target = set()
        for i, b in enumerate(data[0][1:-1]):
            if b == '#':
                self.target.add(i)
        self.buttons = []
        for b in data[1:-1]:
            self.buttons.append(tuple(map(int, b[1:-1].split(','))))

        self.spec_joltage = [int(n) for n in data[-1][1:-1].split(",")]
        self.coef_joltage = [1 for _ in range(len(self.buttons))]

    @staticmethod
    def try_sequence(c) -> set:
        result = set()
        for combo in c:
            for button in combo:
                if button in result:
                    result.remove(button)
                else:
                    result.add(button)
        return result

    def solve_part1(self) -> int:
        presses = 0
        found = False
        for n in range(1, len(self.buttons)):
            for combo in combinations(self.buttons, n):
                if self.try_sequence(combo) == self.target:
                    found = True
                    presses = n
            if found:
                break
        return presses

    def solve_part2(self):
        n = len(self.spec_joltage)
        m = len(self.buttons)

        a = np.zeros((n, m), dtype=int)
        for j, idx in enumerate(self.buttons):
            for i in idx:
                a[i, j] = 1

        jolts = np.array(self.spec_joltage, dtype=float)
        constraints = LinearConstraint(a, lb=jolts, ub=jolts)
        bounds = Bounds(lb=np.zeros(m), ub=np.full(m, np.inf))

        # PyCharm erroneously claims arg c wants an int, when it mos def wants a 1d array.
        # noinspection PyTypeChecker
        result = milp(c=self.coef_joltage,
                      constraints=[constraints],
                      integrality=1,
                      bounds=bounds)

        if result.status != 0:
            raise RuntimeError(
                f"optimization failed with status {result.status}: {result.message}")

        return sum(result.x)


p1_total = 0
p2_total = 0
for line in lines:
    p1_total += Machine(line).solve_part1()
    p2_total += Machine(line).solve_part2()

# Part 1
print(p1_total)
# Part 2
print(int(p2_total))
