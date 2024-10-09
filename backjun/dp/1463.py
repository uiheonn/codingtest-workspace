import time
import sys

n = int(input())
sys.setrecursionlimit(10**9)
    
# 11 -> 10 -> 9 -> 3 -> 1
# 11 -> 10 -> 5 -> 4 -> 2 -> 1

# 10 -> 5 -> 4 -> 2 -> 1
# 10 -> 9 -> 3 -> 1

# 7 -> 6 -> 3 -> 1
# 7 -> 6 -> 3 -> 2

# 6 -> 2 -> 1
# 6 -> 3 -> 2 -> 1
# 6 -> 5 -> 4 -> 2 -> 1

memoList = [0 for _ in range(n)]

def calcul(cnt): # cnt = 11, times = 0
    global memoList

    if cnt == 1:
        return 1
    
    if memoList[cnt - 1] == 0:
        a,b,c = 1000000, 1000000, 0

        if cnt % 3 == 0:
            a = calcul(cnt//3)
        if cnt % 2 == 0:
            b = calcul(cnt//2)
        c = calcul(cnt-1)

        min_val = min(a,b,c)
        memoList[cnt - 1] = min_val

    return memoList[cnt - 1] + 1

# start_time = time.time()
print(calcul(n) - 1)
# end_time = time.time()
# print("seconds : ", end_time - start_time)