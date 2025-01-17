a,b,c = list(map(int, input().split()))

# b의 개수에 따라 2로 나누어 처리한다
# b가 2이면 연산을 수행하고 값을 올려보낸다

def dac(a,b,c): # a = 10, b = 5 # a = 10, b = 2
    tmp = None
    if b > 2 and b % 2 == 0: # b가 짝수이면
        tmp = dac(a,b//2,c) ** 2
    elif b > 2 and b % 2 == 1: # b가 홀수이면
        tmp = dac(a,b//2,c) ** 2 * a
    elif b == 2:
        tmp = a ** 2 # 100
    else:
        tmp = a
    return tmp % c

result = dac(a,b,c)
print(result)