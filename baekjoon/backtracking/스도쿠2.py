import sys

input = sys.stdin.readline
lst = []
for _ in range(9):
    tmp = input()
    semi = []
    for i in range(9):
        semi.append(int(tmp[i]))
    lst.append(semi)

data = [1,2,3,4,5,6,7,8,9]

def check(row, col, sdoku):
    semi = []
    # 수평
    for i in range(9):
        if sdoku[row][i] != 0:
            semi.append(sdoku[row][i])
    # 수직
    for i in range(9):
        if sdoku[i][col] != 0:
            semi.append(sdoku[i][col])
    # 3x3 내부에 있는가
    startRow = row//3 * 3
    startCol = col//3 * 3
    for i in range(startRow, startRow+3):
        for j in range(startCol, startCol+3):
            if sdoku[i][j] != 0:
                semi.append(sdoku[i][j])
    return sorted(list(set(data) - set(semi)))

def oneMoreCheck(row, col, check_num, sdoku):
    # 수평
    for i in range(9):
        if sdoku[row][i] == check_num:
            return True
    # 수직
    for i in range(9):
        if sdoku[i][col] == check_num:
            return True
    # 3x3 내부에 있는가
    startRow = row//3 * 3
    startCol = col//3 * 3
    for i in range(startRow, startRow+3):
        for j in range(startCol, startCol+3):
            if sdoku[i][j] == check_num:
                return True
    return False
    
result = []
def dp(row,col,sdoku):
    if row == 9:
        for i in range(9):
            for j in range(9):
                print(sdoku[i][j],end="")
            print()
        exit()
    
    next_row = row
    next_col = col + 1
    if next_col == 9:
        next_row = row + 1
        next_col = 0

    if sdoku[row][col] != 0: # 0이 아니면 다음 칸으로 이동
        dp(next_row, next_col, sdoku)
    else:
        check_lst = check(row,col,sdoku)
        for check_num in check_lst:
            sdoku[row][col] = check_num
            dp(next_row, next_col, sdoku)
            sdoku[row][col] = 0

dp(0,0,lst)