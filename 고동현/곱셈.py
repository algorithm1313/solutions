a,b,c = map(int,input().split())

def mod_pow(a,b,c):
    result = 1
    a = a%c
    while b > 0:
        if b % 2 == 1:
            result = (result*a) % c
        a = (a * a) %c
        b //= 2
    return result

print(mod_pow(a,b,c))

#print(pow(a,b,c)) -> 파이썬은 내장함수에 모듈러 거듭제곱 pow가 있음.