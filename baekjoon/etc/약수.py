n = int(input()) # 4
temp = list(map(int, input().split())) # [2,3,6,4]
sort = sorted(temp)

if n % 2 == 0: # 짝수이면
    print(sort[0] * sort[-1])
else: # 홀수이면
    print(sort[int(len(sort)/2)] * sort[int(len(sort)/2)])