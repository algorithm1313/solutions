def solution(dirs):
    x, y = 0, 0
    visited = set()
    
    for dir in dirs:
        nx, ny = x, y
        if dir == "U" and y < 5:
            ny = y + 1
        elif dir == "D" and y > -5:
            ny = y - 1
        elif dir == "R" and x < 5:
            nx = x + 1
        elif dir == "L" and x > -5:
            nx = x - 1
        
        if (x, y) != (nx, ny):
            
            visited.add(((min(x, nx), min(y, ny)), (max(x, nx), max(y, ny))))
            print(x,y)
            print(nx, ny)
            x, y = nx, ny
    
    return len(visited)

# def solution(dirs):
#     answer = [0]*2
#     ss=[]
#     for i in dirs:
#         if i=="U" and answer[0] < 5:
#             answer[0] = answer[0]+1
            
#         elif i=="D" and answer[0] >-5:
#             answer[0] = answer[0]-1
            
#         elif i=="R" and answer[1] <5:
#             answer[1] = answer[1]+1
            
#         elif i=="L" and answer[1] > -5:
#             answer[1] = answer[1]-1
            
#         ss.append([answer[0],answer[1]])
        
#     ss = list(set(tuple(item) for item in ss))
#     print(ss)
#     return len(ss)