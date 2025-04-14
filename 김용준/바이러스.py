import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

g = {}
for i in range(1, n+1):
    g[i] = []  

for i in range(m):
    node, edge = map(int, sys.stdin.readline().strip().split())
    g[node].append(edge)
    g[edge].append(node)

visited = [] 
stack = [1]  

while stack:
    current = stack.pop() 
    
    if current not in visited: 
        visited.append(current) 
        
        for next_node in g[current]: 
            if next_node not in visited: 
                stack.append(next_node) 

print(len(visited) - 1)
