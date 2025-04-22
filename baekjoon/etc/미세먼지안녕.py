import sys

input = sys.stdin.readline
r,c,t = map(int, input().split())
lst = []
cleaner = []
for i in range(r):
    tmp = list(map(int, input().split()))
    lst.append(tmp)
    if tmp[0] == -1:
        cleaner.append([i,0])

dx = [0,1,0,-1]
dy = [-1,0,1,0]
for q in range(1,t+1): # 시간 측정
    # 미세먼지 전파
    semi = []
    for i in range(r):
        for j in range(c):
            if lst[i][j] > 0: # 미세먼지가 존재하는 공간이면 저장해놓기
                semi.append([i,j])

    data = []
    for ele in semi:
        ii,jj = ele
        spread = lst[ii][jj] // 5
        for k in range(4):
            nx,ny = ii + dx[k], jj + dy[k]
            if 0 <= nx < r and 0 <= ny < c and lst[nx][ny] != -1:
                data.append([nx,ny,spread])
                lst[ii][jj] -= spread
    for ele in data:
        ii,jj,sp = ele
        lst[ii][jj] += sp

    ct_row, ct_col = cleaner[0]
    ct_col+=1
    tmp = lst[ct_row][ct_col]
    lst[ct_row][ct_col] = 0
    for i in range(1, c-1): # 1. 우측 이동
        res = lst[ct_row][i+1] # 우측 미세먼지 임시 저장
        lst[ct_row][i+1] = tmp
        tmp = res
    for i in range(ct_row,0,-1): # 2. 위로 이동
        res = lst[i-1][-1] # 상단 미세먼지 임시 저장
        lst[i-1][-1] = tmp
        tmp = res
    for i in range(c-1,0,-1): # 3. 좌측 이동
        res = lst[0][i-1]
        lst[0][i-1] = tmp
        tmp = res
    for i in range(0, ct_row-1): # 4. 하단 이동
        res = lst[i+1][0]
        lst[i+1][0] = tmp
        tmp = res
    lst[ct_row][0] = -1

    cb_row, cb_col = cleaner[1]
    cb_col+=1
    tmp = lst[cb_row][cb_col]
    lst[cb_row][cb_col] = 0
    for i in range(1, c-1): # 1. 우측 이동
        res = lst[cb_row][i+1]
        lst[cb_row][i+1] = tmp
        tmp = res
    for i in range(cb_row,r-1): # 2. 하단 이동
        res = lst[i+1][-1]
        lst[i+1][-1] = tmp
        tmp = res
    for i in range(c-1,0,-1): # 3. 좌측 이동
        res = lst[-1][i-1]
        lst[-1][i-1] = tmp
        tmp = res
    for i in range(r-1,cb_row,-1): # 4. 위로 이동
        res = lst[i-1][0]
        lst[i-1][0] = tmp
        tmp = res
    lst[cb_row][0] = -1
    
    semi.clear()
    data.clear()

result = 2
for ele in lst:
    result += sum(ele)
print(result)