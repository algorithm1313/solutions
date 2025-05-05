from itertools import combinations
s = []
for _ in range(9):
    a = int(input())
    s.append(a)

for comb in combinations(s, 7):
    if sum(comb) ==100:
        for i in comb:
            print(i)
        break