def solution(x, n):
    answer = []
    a = x
    for _ in range(n):
        answer.append(a)
        a += x
        print(a)
    return answer

# x = 2
# n = 5
# print(solution(x,n))
