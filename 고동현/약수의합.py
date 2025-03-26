def solution(n):
    list = [n]
    for i in range(1,n):
        if n % i == 0:
            list.append(i)
    answer = sum(list)
    return answer

# n = int(input())
# print(solution(n))

