import sys
input = sys.stdin.readline
n = int(input())


top = list(map(int, input().split()))

stack=[]
answer=[0]*n

for i in range(n-1, -1, -1):
    while stack and top[stack[-1]] < top[i]:
        answer[stack[-1]] = i + 1
        stack.pop()
        
    stack.append(i)
print(' '.join(map(str, answer))) # or print(*answer)