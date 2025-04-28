import math

# yellow = (x-2)(y-2)
# brown = 2x + 2y - 4
# y = 0.5 * brown + 2 - x

def solution(brown, yellow):
    answer = []
    x = 0.5*((2+brown/2) + math.sqrt((2+brown/2) ** 2 - 4*brown - 4*yellow))
    y = 0.5*brown - x + 2
    answer.append(x)
    answer.append(y)
    return answer

# b,y = map(int,input().split())
# solution(b,y)