import sys
from itertools import combinations

l, c = map(int, sys.stdin.readline().strip().split())
strs = sorted(sys.stdin.readline().strip().split())  
vowels = ['a', 'e', 'i', 'o', 'u']

for comb in combinations(strs, l):
    result = ''.join(comb)
    
    vowel_count = sum(1 for char in result if char in vowels)
    consonant_count = sum(1 for char in result if char not in vowels)
    
    if vowel_count >= 1 and consonant_count >= 2:
        print(result)  
