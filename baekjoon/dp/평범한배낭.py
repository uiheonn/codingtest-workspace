import sys

input = sys.stdin.readline
n,k = map(int, input().split()) # n은 물품의 개수, k는 버틸 수 있는 무게
lst = []
for _ in range(n):
    w,v = map(int, input().split()) # w는 무게, v는 가치
    lst.append([w,v])

lst.sort(key = lambda x:x[0])
memo = dict()

for ele in lst:
    weight, value = ele # 4 7
    keys = list(memo.keys())
    semi_lst = [] # 현재 딕셔너리를 모두 계산한 다음 데이터를 변경해야해서 임시 데이터 저장 배열 생성
    for key in keys:
        if key + weight <= k:
            semi_lst.append([key+weight, max(memo.get(key,0)+value, memo.get(key+weight, 0))])
    for key in semi_lst:
        memo[key[0]] = key[1]
    if weight <= k:
        memo[weight] = max(memo.get(weight, 0), value)

max_value = 0
for ele in memo.values():
    if ele > max_value:
        max_value = ele
print(max_value)