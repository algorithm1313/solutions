def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0 and i == ')':
            return False
        if i == '(':
            stack.append(i)
        else:
            if stack[-1] == '(':
                stack.pop()
    if stack:
        return False
    else:
        return True
