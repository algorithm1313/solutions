from itertools import combinations

l, c = map(int, input().split())
s = input().split()
s.sort()

v = ['a', 'e', 'i', 'o', 'u']  

for comb in combinations(s, l):
    v_count = 0
    count = 0
    
    for char in comb:
        if char in v:
            v_count += 1
        else:
            count += 1

    if v_count >= 1 and count >= 2:
        print(''.join(comb))