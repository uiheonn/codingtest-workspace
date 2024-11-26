A = list(map(int, input().split())) # 1 1
B = list(map(int, input().split())) # 2 2

result = 0
if A[0] != 0 and A[1] != 0:
    print(2)
else:
    if A[0] == 0:
        if B[0] == 0 and B[1] < A[1]:
            print(3)
        else:
            print(1)
    elif A[1] == 0:
        if B[1] == 0 and B[0] < A[0]:
            print(3)
        else:
            print(1)
    else:
        print(1)


