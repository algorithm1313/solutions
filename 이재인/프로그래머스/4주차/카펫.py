import math
def solution(brown, yellow):
    answer=[0,0]
    div=0
    y=0
    while True:
        if brown == (y+2+div)*2:
            answer[0] = y+2
            answer[1] = div +2
            break
        div+=1
        y = yellow / div   

    return answer