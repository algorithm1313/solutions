def solution(numbers):
    n = len(numbers)
    result = [-1] * n
    stack = []
    
    for i in range(n):
        while stack and numbers[stack[-1]] < numbers[i]:
            result[stack.pop()] = numbers[i]
        stack.append(i)
        
    return result
