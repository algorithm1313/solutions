# n = int(input())
# li=[]
# for i in range(n):
#     a = int(input())
#     li.append(a)
# answer = 0
# max_stick = 0
# for i in range(n-1, -1, -1):
#     if max_stick < li[i]:
#         max_stick = li[i]
#         answer+=1
# print(answer)

import sys
input = sys.stdin.readline

n = int(input().strip())
li = []

for _ in range(n):
    li.append(int(input().strip()))

answer = 0
max_stick = 0

for i in range(n-1, -1, -1):
    if max_stick < li[i]: 
        max_stick = li[i] 
        answer += 1  

print(answer)
