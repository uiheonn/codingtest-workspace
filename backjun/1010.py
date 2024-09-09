total = int(input())
result = []

def permutation(num):
    tmp = 1
    while num!=0:
        tmp*=num
        num-=1
    return tmp

for i in range(total):
    bridge = input().split() # 1 5
    # nCm = n!/m!(n-m)!
    n = permutation(int(bridge[1]))
    m = permutation(int(bridge[0]))
    nm = permutation(int(bridge[1]) - int(bridge[0]))
    res = n/(m * nm)
    result.append(int(res))
    
print("\n".join(map(str, result)))

# 조합 공식 nCm의 경우
# n!
# /
# m! (n-m)!

# 1. 순열 알고리즘을 구현한다
# 2. 조합 공식을 적용한다

