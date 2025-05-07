def solution(survey, choices):
    answer = ''
    tfmn={"T":0, "F":0, "M":0, "N":0, "R":0, "C":0, "J":0, "A":0}
    
    
    for i in range(len(choices)):
        if choices[i] == 4:
            continue
        elif choices[i] > 4:
            tfmn[survey[i][1]] += (choices[i]%4)
        elif choices[i] < 4:
            tfmn[survey[i][0]]+=(4-choices[i])
    
    def get_max_key(tfmn, key1, key2):
        return key1 if tfmn[key1] >= tfmn[key2] else key2


    answer+=get_max_key(tfmn, 'R', 'T') 
    answer+=get_max_key(tfmn, 'C', 'F')
    answer+=get_max_key(tfmn, 'J', 'M')
    answer+=get_max_key(tfmn, 'A', 'N')
    
    return answer