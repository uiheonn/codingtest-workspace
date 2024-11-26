inp = list(map(int, input().split()))
N = inp[0]
M = inp[1]

location = []
for i in range(N):
    ele = []
    for j in range(N):
        ele.append(True)
    location.append(ele)

def deleteLocation(row, col, direction):
    global location
    if direction == 1: # 위쪽에 있다
        for i in range(N):
            for j in range(N):
                if j != col:
                    location[i][j] = False
                else:
                    if i > row:
                        location[i][j] = False

    elif direction == 5: # 아래에 있다
        for i in range(N):
            for j in range(N):
                if j != col:
                    location[i][j] = False
                else:
                    if i <= row:
                        location[i][j] = False

    elif direction == 3: # 우측에 있다
        for i in range(N):
            for j in range(N):
                if i != row:
                    location[i][j] = False
                else:
                    if j <= col:
                        location[i][j] = False

    elif direction == 7: # 좌측에 있다        
        for i in range(N):
            for j in range(N):
                if i != row:
                    location[i][j] = False
                else:
                    if j >= col:
                        location[i][j] = False
                        
    elif direction == 2:
        for i in range(row, N):
            for j in range(N):
                location[i][j] = False
        for ele in location:
            for j in range(N):
                for i in range(col):
                    location[j][i] = False
    elif direction == 4:
        for i in range(row+1):
            for j in range(N):
                location[i][j] = False
        for ele in location:
            for j in range(N):
                for i in range(col+1):
                    location[j][i] = False
    elif direction == 6:
        for i in range(row+1):
            for j in range(N):
                location[i][j] = False
        for ele in location:
            for j in range(N):
                for i in range(col, N):
                    location[j][i] = False
    elif direction == 8:
        for i in range(row, N):
            for j in range(N):
                location[i][j] = False
        for ele in location:
            for j in range(N):
                for i in range(col, N):
                    location[j][i] = False

for i in range(M):
    nachim = list(map(int, input().split())) # 1 1 4 -> (1, 1)에 나침반을 놓았는데 나침반 4방향을 가리킴
    deleteLocation(nachim[0]-1, nachim[1]-1, nachim[2])
    # for ele in location:
    #     print(ele)

for i in range(N):
    for j in range(N):
        if location[i][j] == True:
            print(i+1,j+1)
            break