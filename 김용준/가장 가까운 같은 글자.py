def solution(s):
    str_stack = []
    answer = []
    for i in range(len(s)):
        if s[i] not in str_stack:
            str_stack.append(s[i])
            answer.append(-1)
        else:
            indices = [j for j, x in enumerate(str_stack) if x == s[i]]
            str_stack.append(s[i])
            answer.append(i - indices[-1])
    return answer
