def solution(n):
    li = []
    while n > 0:
        
        nam = n % 10
        n = n/10
        li.append(nam)
    return li
