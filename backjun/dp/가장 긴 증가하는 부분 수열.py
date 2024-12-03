import sys
# 1. dp로 문제 해결
# 2. 만약 해당 수에 대한 배열이 없다 -> 배열 생성
# 3. i항에 대해 배열을 돌면서 리스트에 추가할지 선택한다
# 3-1. i항이 배열의 첫 항보다 작다 -> 첫 항에 insert
# 3-2. 넣을 배열이 존재하지 않는다 -> 배열을 생성
# 3-3. 넣을 배열은 존재하지 않지만 해당 값보다 큰 수가 포함된 배열이 존재한다 -> 존재하는 큰수를 모두 + 해당 값을 slice하여 새로운 배열을 만든다
# 함수는 해당 배열에 대한 최소값을 리턴한다

# n = int(input())
# lst = list(map(int, input().split())) # 10 20 10 30 20 50

input = sys.stdin.read
Data = input().splitlines()
n = int(Data[0])
lst = list(map(int, Data[1].split()))

global data
data = set()
res = tuple([lst[-1]])
data.add(res)
def dp(start):
    global data
    startNum = lst[start] # 20
    appendData = []

    for ele in data: # 새로운 배열을 생성하는지 체크 -> 맞으면 아래 for문은 수행하지 않는다
        if not ele:
            continue

        if ele[-1] > startNum: # 넣어야 하는 경우
            new_list = list(ele)
            new_list.append(startNum)
            appendData.append(tuple(new_list))
        elif ele[0] > startNum: # 사이값인 경우
            count = 0
            for i in ele:
                if startNum >= i:
                    break
                else:
                    count+=1
            lsls = list(ele[:count])
            lsls.append(startNum)
            appendData.append(tuple(lsls))
    for ele in appendData:
        data.add(ele)
                    
    if not any(ele[0] > startNum for ele in data):
        data.add(tuple([startNum]))

for i in range(n-2,-1,-1):
    dp(i)

maxNum = 0
for i in data:
    if len(i) > maxNum:
        maxNum = len(i)

# print(data)
print(maxNum)