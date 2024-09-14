# 첫번째 퀸부터 반복문을 통해 이동하며 퀸을 놓고 그 아래로 이동한다
n = int(input())

def isCross(ele, row, col): # ele=[0,1]인 경우 대각선에 있는지 확인
    return abs(ele[0] - row) != abs(ele[1] - col)

def checkQueenLocation(queenList, row, col): # row, col에 queen을 넣어도 되는지 확인
    for ele in queenList:
        if ele[0] == row or ele[1] == col or not isCross(ele, row, col):
            return False
    return True

total = 0
def backTracking(queenList, n, row):
    global total
    
    if row == n:
        total+=1
        return
        
    for i in range(n): # row항 i열을 0부터 끝까지 돌려서 퀸을 넣을 수 있는지 확인
        if checkQueenLocation(queenList, row, i):
            backTracking(queenList + [[row, i]], n, row+1)

for col in range(0, n): # col열에 퀸을 놓을 차례
    queenList = [[0, col]] # 0항 col열에 퀸을 놓을 상태로 백트래킹 시작
    backTracking(queenList, n, 1) # 경우의 수를 리턴

print(total)