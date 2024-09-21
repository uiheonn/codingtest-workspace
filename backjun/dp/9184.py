import sys

input = sys.stdin.readline
output = sys.stdout.write

dpList = [[[0] * (21) for _ in range(21)] for _ in range(21)]
def dp(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return dp(20, 20, 20)
    if dpList[a][b][c]:
        return dpList[a][b][c]
    if a < b < c:
        dpList[a][b][c] = dp(a,b,c-1) + dp(a,b-1,c-1) - dp(a,b-1,c)
        return dpList[a][b][c]
    dpList[a][b][c] = dp(a-1,b,c) + dp(a-1,b-1,c) + dp(a-1,b,c-1) - dp(a-1,b-1,c-1)
    return dpList[a][b][c]

while True:
    a,b,c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break
    output(f"w({a}, {b}, {c}) = {dp(a, b, c)}\n")
