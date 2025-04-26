def solution(s):
    if s[0] == ')' or s[-1] == '(':
        return False
    stack = []
    for x in s:
        if x == '(':
            stack.append(x)
        elif x == ')':
            if len(stack) == 0:
                return False
            stack.pop(-1)
    
    if stack:
        return False
    else:
        return True

s = "()()"
print(solution(s))