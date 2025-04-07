# import sys
# from math import factorial as fact

# input = sys.stdin.readline

# n,m =map(int, input().split())
# def zeroout(n,m):
#     if n == 0:
#         return 1
#     if m == 0:
#         return 1
#     if n < m:
#         return 0
#     return fact(n)//(fact(m)*fact(n-m))
# print((str(zeroout(n,m)).count('0'))) #끝자리만 세야하는데?:">"

def t_f_count(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count

n, m = map(int, input().split())

if m == 0:
    print(0)
else:
    t_ = t_f_count(n, 2) - t_f_count(m, 2) - t_f_count(n-m, 2)
    f_ = t_f_count(n, 5) - t_f_count(m, 5) - t_f_count(n-m, 5)

    print(min(t_, f_))