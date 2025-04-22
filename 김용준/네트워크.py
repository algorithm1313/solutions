def solution(n, computers):
    visited = set()
    network = 0
    
    for i in range(n):
        if i in visited:
            continue
            
        network += 1
        stack = [i]
        
        while stack:
            current_node = stack.pop()
            
            if current_node not in visited:
                visited.add(current_node)
                
                for next_node in range(n):
                    if computers[current_node][next_node] == 1 and next_node not in visited:
                        stack.append(next_node)
    
    return network
