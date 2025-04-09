from itertools import product

def solution(numbers, target):
    opers = [1, -1] 
    combs = list(product(opers, repeat=len(numbers)))
    
    count = 0
    for comb in combs:
        total = 0
        for i in range(len(comb)):
            total += comb[i] * numbers[i] 
        
        if total == target:
            count += 1
    
    return count
