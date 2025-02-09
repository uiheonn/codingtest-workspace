n = int(input())
for _ in range(n):
    M,N,x,y = map(int, input().split())
    tmp = x
    right = False
    while tmp <= M * N:
        if (tmp-x) % M == 0 and (tmp-y) % N == 0:
            print(tmp)
            right = True
            break
        tmp+=M
    if not right:
        print(-1)