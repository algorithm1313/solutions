def solution(dirs):
    move = {
          'U': (0, 1), 
          'D': (0, -1), 
          'R': (1, 0),
          'L': (-1, 0)}
        
    worked = set()
    x, y = 0, 0
    for d in dirs:
        dx, dy = move[d]
        newx = x+ dx
        newy = y +dy
        if -5<= newx <= 5 and -5<= newy <= 5:
            worked.add(((x,y), (newx,newy)))
            worked.add(((newx,newy),(x,y)))
            x=newx
            y=newy

    return len(worked) //2   #(a->b), (b->a) 모두 구했기 때문에 2로 나누기 