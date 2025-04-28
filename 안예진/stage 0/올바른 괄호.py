def solution(s):
    a = [] # 비어있는 리스트
    
    for b in s:        
        if b == '(': #만약 여는 괄호면 스택
            a.append(b)
        elif b == ')': #닫는 괄호면
            if not a: #스택 안에 아무것도 없으면 쌓이먄 안됨
                return False
            a.pop() #여는 괄호 제거
    
    
    return len(a) == 0 #여는 괄호가 없다 ( =>남아있지 않다 Tru