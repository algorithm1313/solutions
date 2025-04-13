import sys

def dfs(idx):
    global visited
    visited[idx] = True
    print(idx, end=' ')
    for i in range(1, n+1):
        if graph[idx][i] and not visited[i]:
            dfs(i)


def bfs():
    global q, visited
    while q:
        cur = q.pop(0)
        print(cur, end=' ')
        for i in range(1, n+1):
            if graph[cur][i] and not visited[i]:
                q.append(i)
                visited[i] = True

input = sys.stdin.readline
n, m, v = map(int, input().split())

graph = [[False] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

# 1. graph 정보
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

# 2. dfs
dfs(v)
print()

# 3. BFS
visited = [False] * (n+1)
q = [v]
visited[v] = True
bfs()
print()