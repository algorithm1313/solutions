
def aa(docu, word) : #문서, 단어로 비교 함수    
    cnt = 0 #같으면 저장할 변수
    ind = 0 #위치 대조를 위한 변수
    while True:
        #단어가 문거에서 나오는 위치
        ind =docu.find(word,ind)  #. find에 찾아는거 신기,,,
    
        #단어가 업슴ㄴ 종료
        if ind == -1:
            break
          
        #단어 발견 시 1 증가
        cnt +=1
            
        #중복을 피하기 위한 위치 설정!
        ind += len(word)
    return cnt
   
   
   
   
doc = input().strip()
word = input().strip()

print(aa(doc, word))