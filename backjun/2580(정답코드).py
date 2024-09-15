import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
output = sys.stdout.write

# 스도쿠 판 정의
sdoku = []
for i in range(9):
    sdoku.append(list(map(int, input().rstrip().split())))

# 행, 열, 3x3 영역에 대한 캐시 저장
row_cache = [set() for _ in range(9)]
col_cache = [set() for _ in range(9)]
three_cache = [[set() for _ in range(3)] for _ in range(3)]

# 초기화: 미리 채워진 값들로 캐시 세팅
for i in range(9):
    for j in range(9):
        if sdoku[i][j] != 0:
            row_cache[i].add(sdoku[i][j])
            col_cache[j].add(sdoku[i][j])
            three_cache[i // 3][j // 3].add(sdoku[i][j])

def backtracking(idx):
    # 모든 칸을 다 채웠으면 종료
    if idx == 81:
        return True
    
    row = idx // 9
    col = idx % 9
    
    # 이미 값이 채워져 있는 칸이면 다음 칸으로
    if sdoku[row][col] != 0:
        return backtracking(idx + 1)
    
    # 가능한 숫자 찾기
    for num in range(1, 10):
        if (num not in row_cache[row] and 
            num not in col_cache[col] and 
            num not in three_cache[row // 3][col // 3]):
            
            # 해당 숫자를 채우고 캐시에 기록
            sdoku[row][col] = num
            row_cache[row].add(num)
            col_cache[col].add(num)
            three_cache[row // 3][col // 3].add(num)
            
            # 다음 칸을 백트래킹
            if backtracking(idx + 1):
                return True
            
            # 실패하면 해당 숫자 제거 (백트래킹)
            sdoku[row][col] = 0
            row_cache[row].remove(num)
            col_cache[col].remove(num)
            three_cache[row // 3][col // 3].remove(num)
    
    return False

# 백트래킹 시작
backtracking(0)

# 결과 출력
output("\n".join(" ".join(map(str, row)) for row in sdoku) + "\n")