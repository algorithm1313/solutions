import sys
input = sys.stdin.readline

def power(a, b, c):
    if b == 0:
        return 1
    elif b == 1:
        return a % c
    
    temp = power(a, b//2, c)
    if b % 2 == 0:
        return (temp * temp) % c
    else:
        return (temp * temp * a) % c

a, b, c = map(int, input().split())
print(power(a, b, c))