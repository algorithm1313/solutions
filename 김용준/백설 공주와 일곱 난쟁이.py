from itertools import combinations
import sys

dwarfs = []
for i in range(9):
    dwarfs.append(int(sys.stdin.readline().strip()))

for comb in combinations(dwarfs, 7):
    if sum(comb) == 100:
        answer = list(comb)
        break
        
for dwarf in sorted(answer):
    print(dwarf)
