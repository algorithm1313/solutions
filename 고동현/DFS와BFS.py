def dfs(idx):
    global visited
    visited[idx] = True
    print(idx, end = ' ')
    for next in range(1, N+1):
        if not visited[next] and graph[idx][next]:
            dfs(next)

def bfs():
    global q, visited
    while q:
        cur = q.pop(0)
        print(cur, end = ' ')
        for next in range(1, N+1):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                q.append(next)


# 입력 및 초기화
# N = 정점의 개수, M = 간선의 갯수, V = 탐색 시작 정점의 번호
N, M, V = map(int,input().split())

graph = [[False]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)

for i in range(M):
    node, edge = map(int, input().split())
    graph[node][edge] = True
    graph[edge][node] = True

# dfs
dfs(V)
print()

# bfs
visited = [False]*(N+1)
q = [V]
visited[V] = True
bfs()
