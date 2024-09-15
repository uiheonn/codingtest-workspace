# 1. 1행1열부터 이동하며 채울 수 있는지 확인
# 2. 채울 수 있다면 채우고, 만약 채울 수 없는 경우라면
#    비어있는 값으로 이동하여 채울 수 있는지 이동한다
# 3. 값을 채울 수 있을 때까지 이동한다(백트래킹)
# 4. 채우고 기존 위치까지 돌아온다
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
output = sys.stdout.write

sdoku = []
for i in range(9):
    inp = list(map(int, input().rstrip().split()))
    sdoku.append(inp)

def backtracking(row, col, beforDirection):
    fullSet = set(range(1,10))
    rowSet = set()
    colSet = set()
    threeSet= set()
    # 같은 항 중 비어있는게 있다면 글로 이동(해당 열의 우측부터 시작)
    if beforDirection != "col":
        for i in range(9):
            if i != col:
                colSet.add(sdoku[row][i])
        
        missingNumberCol = list(fullSet - colSet)
        if len(missingNumberCol) == 1:
            sdoku[row][col] = missingNumberCol[0] if missingNumberCol else None
            return

    # 같은 열 중 비어있는게 있다면 글로 이동(해당 항의 하단부터 시작)
    if beforDirection != "row":
        for i in range(9):
            if i != row:
                rowSet.add(sdoku[i][col])
        
        missingNumberRow = list(fullSet - rowSet)
        if len(missingNumberRow) == 1:
            sdoku[row][col] = missingNumberRow[0] if missingNumberRow else None
            return
    
    # 3x3 이내에 비어있는게 있다면 글로 이동(해당 항열의 우측부터 시작)
    # row = 3, col = 5
    rowStart = (row // 3) * 3
    colStart = (col // 3) * 3
    if beforDirection != "three":
        for i in range(rowStart, rowStart + 3):
            for j in range(colStart, colStart + 3):
                if i == row and j == col:
                    continue
                threeSet.add(sdoku[i][j])
        
        missingNumberThree = list(fullSet - threeSet)
        if len(missingNumberThree) == 1:
            sdoku[row][col] = missingNumberThree[0] if missingNumberThree else None
            return
    
    # 수를 채울 수 없다면 다른 곳으로 백트래킹
    for i in range(col+1, 9):
        if i > col and sdoku[row][i] == 0:
            backtracking(row, i, "col")
    
    for i in range(row+1, 9):
        if i > row and sdoku[i][col] == 0:
            backtracking(i, row, "row")

    for i in range(rowStart, rowStart + 3):
        for j in range(colStart, colStart + 3):
            if i == row and j == col:
                continue
            elif sdoku[i][j] == 0:
                backtracking(i, j, "three")

for row in range(9):
    for col in range(9):
        if sdoku[row][col] == 0: # 비어있는 값이면
            backtracking(row, col, None)

output("\n".join(" ".join(map(str, sdoku[i])) for i in range(9)) + "\n")
