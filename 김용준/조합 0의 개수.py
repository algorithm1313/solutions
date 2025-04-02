import sys
from math import factorial

n, m = map(int, sys.stdin.readline().split())

def count_k(n, k):
    count = 0
    while n > 0:
        n = n // k
        count += n
    return count

twos = count_k(n, 2) - count_k(m, 2) - count_k(n - m, 2)
fives = count_k(n, 5) - count_k(m, 5) - count_k(n - m, 5)

print(min(twos, fives))
