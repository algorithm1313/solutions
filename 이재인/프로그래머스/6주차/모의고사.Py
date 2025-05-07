def solution(answers):
    answer = [0]*3
    user1 = [1,2,3,4,5]
    user2 = [2,1,2,3,2,4,2,5]
    user3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        
        if answers[i] == user1[i % len(user1)]:
            answer[0]+=1
        if answers[i] == user2[i % len(user2)]:
            answer[1]+=1
        if answers[i] == user3[i % len(user3)]:
            answer[2]+=1
    max_i = []
    max_v = answer[0]
    for i in range(len(answer)):
        if max_v < answer[i]:
            max_i = []
            max_i.append(i+1)
            max_v = answer[i]
        elif max_v == answer[i]:
            max_i.append(i+1)
            
        
    return max_i