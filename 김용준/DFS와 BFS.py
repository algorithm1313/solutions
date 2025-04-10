import sys
from collections import deque
n, m, start = map(int, sys.stdin.readline().strip().split())
g = {}
for i in range(m):
    node, edge = map(int, sys.stdin.readline().strip().split())
    if node not in g:
        g[node] = [edge]
    else:
        g[node].append(edge)
    
    if edge not in g:
        g[edge] = [node]
    else:
        g[edge].append(node)

if start not in g:
    g[start] = []

for i in g:
    g[i].sort()

def dfs(graph, start):
    visited = []
    stack = [start]
    
    while stack:
        current = stack.pop()  
        if current not in visited:
            visited.append(current)
            print(current, end=' ')
            for next_node in sorted(graph[current], reverse=True):
                if next_node not in visited:
                    stack.append(next_node)

def bfs(graph, start):
    visited = [start]
    q = deque([start])
    
    while q:
        current = q.popleft()
        print(current, end=' ')
        
        for next_node in graph[current]:
            if next_node not in visited:
                visited.append(next_node)
                q.append(next_node)

dfs(g, start)
print()
bfs(g, start)
