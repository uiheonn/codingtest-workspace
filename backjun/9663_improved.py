import sys
input = sys.stdin.read
output = sys.stdout.write

def backTracking(n, row, cols, diag1, diag2):
    global total
    if row == n:
        total += 1
        return

    for col in range(n):
        # 대각선 및 열 체크 (diag1: / 방향 대각선, diag2: \ 방향 대각선)
        if col in cols or (row - col) in diag1 or (row + col) in diag2:
            continue

        # 현재 열과 대각선을 사용 중으로 표시
        cols.add(col)
        diag1.add(row - col)
        diag2.add(row + col)

        # 다음 퀸 배치
        backTracking(n, row + 1, cols, diag1, diag2)

        # 백트래킹 (사용했던 열과 대각선 해제)
        cols.remove(col)
        diag1.remove(row - col)
        diag2.remove(row + col)

def main():
    global total
    n = int(input().strip())
    total = 0
    cols = set()   # 사용된 열
    diag1 = set()  # / 방향 대각선
    diag2 = set()  # \ 방향 대각선

    # 첫 번째 퀸을 첫 번째 행에 배치하고 시작
    backTracking(n, 0, cols, diag1, diag2)

    output(f"{total}\n")

if __name__ == "__main__":
    main()
