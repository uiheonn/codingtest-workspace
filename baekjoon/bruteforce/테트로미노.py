import sys

input = sys.stdin.readline
n,m = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

# ㅡ자 테트로미노
f1dx = [[0,0,0,0],[0,1,2,3]]
f1dy = [[0,1,2,3],[0,0,0,0]]

# ㅁ자 테트로미노
s1dx = [[0,0,1,1]]
s1dy = [[0,1,0,1]]

# ㅗ자 테트로미노
t1dx = [[0,0,0,1],[0,1,2,1],[0,0,-1,1],[0,0,0,-1]]
t1dy = [[0,1,2,1],[0,0,0,1],[0,1,1,1],[0,1,2,1]]

# ㄱㄴ자 테트로미노
z1dx = [[0,0,1,1],[0,0,-1,-1],[0,1,0,-1],[0,1,1,2]]
z1dy = [[0,1,1,2],[0,1,1,2],[0,0,1,1],[0,0,1,1]]

# ㄴ자 테트로미노
x1dx = [[0,0,1,2],[0,0,-1,-2],[0,0,0,1],[0,1,1,1],[0,1,2,2],[0,0,1,2],[0,0,0,1],[0,0,0,-1]]
x1dy = [[0,1,0,0],[0,1,1,1],[0,1,2,2],[0,0,1,2],[0,0,0,1],[0,1,1,1],[0,1,2,0],[0,1,2,2]]

max_sum = 0
result = []
for i in range(n):
    for j in range(m):
        # ㅡ자 확인
        for k in range(2):
            fdx = f1dx[k]
            fdy = f1dy[k]
            right = True
            for q in range(4):
                d1x = i + fdx[q]
                d1y = j + fdy[q]
                if 0 > d1x or d1x >= n or 0 > d1y or d1y >= m:
                    right = False
                    break
            if right:
                sm = lst[fdx[0]+i][fdy[0]+j] + lst[fdx[1]+i][fdy[1]+j] + lst[fdx[2]+i][fdy[2]+j] + lst[fdx[3]+i][fdy[3]+j]
                result.append(sm)
        # ㅁ자 확인
        for k in range(1):
            sdx = s1dx[k]
            sdy = s1dy[k]
            right = True
            for q in range(4):
                d1x = i + sdx[q]
                d1y = j + sdy[q]
                if 0 > d1x or d1x >= n or 0 > d1y or d1y >= m:
                    right = False
                    break
            if right:
                sm = lst[sdx[0]+i][sdy[0]+j] + lst[sdx[1]+i][sdy[1]+j] + lst[sdx[2]+i][sdy[2]+j] + lst[sdx[3]+i][sdy[3]+j]
                result.append(sm)
        # ㅗ자 확인
        for k in range(4):
            tdx = t1dx[k]
            tdy = t1dy[k]
            right = True
            for q in range(4):
                d1x = i + tdx[q]
                d1y = j + tdy[q]
                if 0 > d1x or d1x >= n or 0 > d1y or d1y >= m:
                    right = False
                    break
            if right:
                sm = lst[tdx[0]+i][tdy[0]+j] + lst[tdx[1]+i][tdy[1]+j] + lst[tdx[2]+i][tdy[2]+j] + lst[tdx[3]+i][tdy[3]+j]
                result.append(sm)
        # ㄱㄴ자 확인
        for k in range(4):
            zdx = z1dx[k]
            zdy = z1dy[k]
            right = True
            for q in range(4):
                d1x = i + zdx[q]
                d1y = j + zdy[q]
                if 0 > d1x or d1x >= n or 0 > d1y or d1y >= m:
                    right = False
                    break
            if right:
                sm = lst[zdx[0]+i][zdy[0]+j] + lst[zdx[1]+i][zdy[1]+j] + lst[zdx[2]+i][zdy[2]+j] + lst[zdx[3]+i][zdy[3]+j]
                result.append(sm)
        # ㄴ자 확인
        for k in range(8):
            xdx = x1dx[k]
            xdy = x1dy[k]
            right = True
            for q in range(4):
                d1x = i + xdx[q]
                d1y = j + xdy[q]
                if 0 > d1x or d1x >= n or 0 > d1y or d1y >= m:
                    right = False
                    break
            if right:
                sm = lst[xdx[0]+i][xdy[0]+j] + lst[xdx[1]+i][xdy[1]+j] + lst[xdx[2]+i][xdy[2]+j] + lst[xdx[3]+i][xdy[3]+j]
                result.append(sm)

# print(result)
print(max(result))