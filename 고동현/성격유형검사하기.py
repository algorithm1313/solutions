def solution(survey, choices):
    dict = {'R':0, 'T':0, 
            'C':0, 'F':0,
            'J':0, 'M':0,
            'A':0, 'N':0
            }
    answer = ''
    for i in range(len(choices)):
        if choices[i] == 1:
            dict[survey[i][0]] += 3
        elif choices[i] == 2:
            dict[survey[i][0]] += 2
        elif choices[i] == 3:
            dict[survey[i][0]] += 1
        elif choices[i] == 5:
            dict[survey[i][1]] += 1
        elif choices[i] == 6:
            dict[survey[i][1]] += 2
        elif choices[i] == 7:
            dict[survey[i][1]] += 3
    if dict['R'] >= dict['T']:
        answer += 'R'
    else:
        answer += 'T'

    if dict['C'] >= dict['F']:
        answer += 'C'
    else:
        answer += 'F'
    
    if dict['J'] >= dict['M']:
        answer += 'J'
    else:
        answer += 'M'
    
    if dict['A'] >= dict['N']:
        answer += 'A'
    else:
        answer += 'N'
    return answer

# survey = ["AN", "CF", "MJ", "RT", "NA"]
# choices = [5, 3, 2, 7, 5]
# print(solution(survey,choices))

# dict = {'R':0 , 'C':1}
# dict['C'] += 1
# print(dict['C'])

