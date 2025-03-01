import sys

input = sys.stdin.readline
n = int(input())
dp_lst = []
for _ in range(n):
    dp_lst.append(list(map(int, input().split())))

def dp(row, col, direction):
    global count

    if row >= n or col >= n:
        return
    
    if row == n-1 and col == n-1:
        count+=1
    
    if direction == 0: # 파이프가 수직이라면
        if col+1 < n and dp_lst[row][col+1] != 1: # 우측이 벽이 아니면 2개 모두 가능
            if row+1 < n and dp_lst[row+1][col+1] == 1:
                dp(row, col+1, 0)
            elif row+1 < n and dp_lst[row+1][col] == 1:
                dp(row, col+1, 0)
            else:
                dp(row, col+1, 0)
                dp(row+1, col+1, 2)
    elif direction == 1: # 파이프가 수평이라면
        if row+1 < n and dp_lst[row+1][col] != 1: # 아래가 벽이 아니면 2개 모두 가능
            if col+1 < n and dp_lst[row+1][col+1] == 1:
                dp(row+1, col, 1)
            elif col+1 < n and dp_lst[row][col+1] == 1:
                dp(row+1, col, 1)
            else:
                dp(row+1, col, 1)
                dp(row+1, col+1, 2)
    else: # 파이프가 대각선이라면
        if col+1 < n and dp_lst[row][col+1] == 1: # 우측에 벽이 있는 경우
            if row+1 < n and dp_lst[row+1][col] == 0:
                dp(row+1, col, 1)
        elif row+1 < n and dp_lst[row+1][col] == 1: # 아래에 벽이 있는 경우
            if col+1 < n and dp_lst[row][col+1] == 0:
                dp(row, col, 0)
        elif row+1 < n and col+1 < n and dp_lst[row+1][col+1] == 1: # 대각선에 벽이 있는 경우
            if dp_lst[row][col+1] == 0:
                dp(row, col+1, 0)
            if dp_lst[row+1][col] == 0:
                dp(row+1, col, 1)
        else: # 벽이 없는 경우      
            dp(row, col+1, 0)
            dp(row+1, col, 1)
            dp(row+1, col+1, 2)

if dp_lst[-1][-1] == 1:
    print(0)
else:
    count = 0
    dp(0,1,0)
    print(count)