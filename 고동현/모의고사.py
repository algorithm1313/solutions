from collections import deque

def solution(answers):
    results = [0,0,0]
    supo_1 = deque([1,2,3,4,5])
    supo_2 = deque([2,1,2,3,2,4,2,5])
    supo_3 = deque([3,3,1,1,2,2,4,4,5,5])
    for i in range(len(answers)):
        if answers[i] == supo_1[0]:
            results[0] += 1
        if answers[i] == supo_2[0]:
            results[1] += 1
        if answers[i] == supo_3[0]:
            results[2] += 1
        supo_1.append(supo_1.popleft())
        supo_2.append(supo_2.popleft())
        supo_3.append(supo_3.popleft())
    answer = [i+1 for i,num in enumerate(results) if max(results) == num]
    return answer


# print(solution([1,2,3,4,5]))
# print(solution([1,3,2,4,2]))

