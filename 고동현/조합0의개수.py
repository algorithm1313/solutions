from math import comb
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

combinsation =  comb(n,m)

def countZero(n):
    count = 0
    while n % 10 == 0:
        count += 1
        n //= 10
    return count

print(countZero(combinsation))