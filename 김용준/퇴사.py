import sys

n = int(sys.stdin.readline().strip())
consults = []
for i in range(n):
    time, profit = map(int, sys.stdin.readline().strip().split())
    consults.append([time, profit])

visited = [-1] * (n + 1)

def solution(day):
    if day >= n:
        return 0
    
    if visited[day] != -1:
        return visited[day]
    
    profit = solution(day + 1)
    
    if day + consults[day][0] <= n:
        profit = max(profit, consults[day][1] + solution(day + consults[day][0]))
    
    visited[day] = profit

    return profit

print(solution(0))
