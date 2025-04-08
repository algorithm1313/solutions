def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []  
    
    for i in range(len(numbers)):
        while stack and numbers[i] > numbers[stack[-1]]:
            answer[stack.pop()] = numbers[i]

        stack.append(i)
    
    return answer



# def solution(numbers):
#     answer=[-1]*len(numbers)
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             if numbers[i] < numbers[j]:
#                 answer[i] = numbers[j]
#                 break
#     return answer
# runtime erorr : 89 (이중 for문은 X)

# def solution(numbers):
#     answer=[-1]*len(numbers)
#     for i in range(len(numbers)):
#         n=i
#         while n < len(numbers)-1 :
#             n+=1
#             if numbers[i] < numbers[n]:
#                 answer[i] = numbers[n]
#                 break
#     return answer
# runtime erorr : 83


