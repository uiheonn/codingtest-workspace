n = int(input())
total = list(map(int, input().split()))

# 10 -4 3 1 5 6 -35 12 21 -1
# 1. 현재 위치를 갖고 가리키는 포인터 : now
# 2. sum(list[start:now-1])이 0보다 start = now가 된다
# 3. 합을 항상 계산하며 max를 리턴

# -1 1 10 2 -> -1이 없는 1 10 2로 만들어야 함

start = 0
max = -1001
totalSum = 0
for i in range(n):
    #s = sum(total[start:i]) # 33
    totalSum+=total[i]
    if totalSum < total[i]: # -1 < -2, -1 < 1
        totalSum = total[i]
    if totalSum > max:
        max = totalSum

print(max)