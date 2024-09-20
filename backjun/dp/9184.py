import sys

input = sys.stdin.readline
output = sys.stdout.write

dpList = [[[0] * (21) for _ in range(21)] for _ in range(21)]
def dp(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return dp(20, 20, 20)
    elif a < b < c:
        dpList[a][b][c] = dp(a,b,c-1) + dp(a,b-1,c-1) - dp(a,b-1,c)
        return dpList[a][b][c]
    else:
        dpList[a][b][c] = dp(a-1,b,c) + dp(a-1,b-1,c) + dp(a-1,b,c-1) - dp(a-1,b-1,c-1)
        return dpList[a][b][c]



while True:
    inp = list(map(int, input().split()))
    a = inp[0]
    b = inp[1]
    c = inp[2]
    if a==-1 and b==-1 and c==-1:
        break
    output(f"{a} {b} {c}\n")


