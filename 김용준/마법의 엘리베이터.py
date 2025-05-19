def solution(storey):
    answer = 0
    while storey > 0:
        digit = storey % 10
        next_digit = (storey // 10) % 10

        if digit > 5:
            answer += (10 - digit)
            storey += 10  # 올림 처리
        elif digit < 5:
            answer += digit
        else:  # digit == 5
            if next_digit >= 5:
                answer += 5
                storey += 10  # 올림
            else:
                answer += 5  # 그냥 내림
        storey //= 10

    return answer
