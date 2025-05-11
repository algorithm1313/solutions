def solution(storey):
    result = 0
    while storey > 0:
        num = storey % 10  
        next_num = (storey // 10) % 10  
        
        
        if num > 5 or (num == 5 and next_num >= 5):
            result += 10 - num
            storey = (storey // 10) + 1  
        else:
            result += num
            storey //= 10  
    return result