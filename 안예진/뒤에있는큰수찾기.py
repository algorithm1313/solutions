def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        found = False
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[i]:
                answer.append(numbers[j])
                found = True
                break
        if not found:
            answer.append(-1)
    return answer