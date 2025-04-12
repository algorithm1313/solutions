def solution(numbers, target):
    answer = [0]  

    def re(index, total):
        if index == len(numbers):
            if total == target:
                answer[0] += 1
            return
        re(index + 1, total + numbers[index])
        re(index + 1, total - numbers[index])

    re(0, 0)
    return answer[0]