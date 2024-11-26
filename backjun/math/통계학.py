import sys

input = sys.stdin.read

data = input().splitlines()
total = int(data[0])
result = list(map(int, data[1:]))

def average(sort):
    tmp = 0
    for i in  range(len(sort)):
        tmp+=sort[i]
    return int(round(tmp/len(sort), 0))

def moreable(sort):
    dic = {}
    for i in range(len(sort)):
        if sort[i] in dic:
            dic[sort[i]]+=1
        else:
            dic[sort[i]]=1

    largeKey=list(dic.keys())[0]
    for i in dic.keys():
        if dic[i] > dic[largeKey]:
            largeKey = i
    
    arr=[]
    for i in dic.keys():
        if dic[i] == dic[largeKey]:
            arr.append(i)
    
    cnt=arr[0]

    if len(arr) >= 2:
        cnt=arr[1]

    return cnt

sortResult = sorted(result)

# 산술평균 - 소수점 첫째자리에서 반올림
print(average(sortResult))

# 중앙값
print(sortResult[total//2])

# 최빈값 - 여러개인 경우 2번째로 작은 값으로(딕셔너리 사용)
print(moreable(sortResult))

# 범위
print(sortResult[-1] - sortResult[0])