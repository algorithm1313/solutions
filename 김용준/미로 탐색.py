import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

miro = []
for _ in range(n):
    miro.append(list(map(int, sys.stdin.readline().strip())))
    
visited = [[0] * m for _ in range(n)]

q = deque([(0, 0)])
visited[0][0] = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and miro[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))

print(visited[n-1][m-1])
