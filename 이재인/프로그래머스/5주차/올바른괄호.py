def solution(s):
    answer = True
    if s[0] == ")" or s[-1] == "(":
        return False
    stack=[]
    for i in s:
        if i == "(":
            stack.append(i)
            
        elif i == ")":
            if len(stack) < 1:
                return False
            stack.pop(-1)
            
    if len(stack) == 0:
        return True
    else : 
        return False
    