with open("input.txt", "r") as f:
    lines = f.readlines()

left = []
right = []
for line in lines:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()
pairs = list(zip(left, right))

diffs = []
for pair in pairs:
    if pair[0] > pair[1]:
        diffs.append(pair[0] - pair[1])
    else:
        diffs.append(pair[1] - pair[0])

print(sum(diffs))

# part 2
similarity_score = []
for number in left:
    n = right.count(number)
    similarity_score.append(number * n)

sum(similarity_score)
