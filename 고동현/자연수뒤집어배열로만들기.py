def solution(n):
    answer = []
    string = str(n)
    for s in string:
        answer.append(int(s))
    answer = list(reversed(answer))
    return answer


