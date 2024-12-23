def check_safety(l: list) -> bool:
    diffs = [l[i + 1] -  l[i] for i in range(len(l) - 1)]

    if 0 in diffs:
        return False

    asc = diffs[0] > 0
    dec = diffs[0] < 0
    for n in diffs:
        if asc:
            if not n in [1, 2, 3]:
                return False
        if dec:
            if not n in [-1, -2, -3]:
                return False
    return True

with open("input2.txt", "r") as f:
    lines = f.readlines()

reports = []
for line in lines:
    report = [int(num) for num in line.split()]
    reports.append(report)

safe = 0
natural_safe = 0
for rep in reports:
    if check_safety(rep):
        safe += 1
        natural_safe += 1
    else:
        for i in range(len(rep)):
            r = rep.copy()
            r.pop(i)
            if check_safety(r):
                safe += 1
                break

print(natural_safe)
print(safe)
