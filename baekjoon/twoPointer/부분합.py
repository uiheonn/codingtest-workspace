# l,r 은 0부터 시작
# l,r 모두 n까지 돌았을 때 종료
# 만약 length가 1인걸 찾았다면 바로 종료
# 10 15
# 5 1 3 5 10 7 4 9 2 8
# 5 100
# 1 1 1 1 3000

n,s = map(int, input().split())
lst = list(map(int, input().split()))
l,r = 0,0
summ = lst[0]
min_len = 100001
while r < n:
    if s > summ:
        if r == n-1:
            break
        r+=1
        summ+=lst[r]
    else:
        if l == r:
            min_len = 1
            break
        if r-l+1 < min_len:
            min_len = r-l+1
        summ-=lst[l]
        l+=1
if min_len == 100001:
    min_len = 0
print(min_len)