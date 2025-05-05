def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    answers_count = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == one[i % 5]:
            answers_count[0] += 1
        if answers[i] == two[i % 8]:
            answers_count[1] += 1
        if answers[i] == three[i % 10]:
            answers_count[2] += 1
    
    supoja = []
    for i in range(len(answers_count)):
        if answers_count[i] == max(answers_count):
            supoja.append(i + 1)
    
    return supoja
