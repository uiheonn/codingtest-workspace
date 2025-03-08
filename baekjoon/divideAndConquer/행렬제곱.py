import sys
import collections

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
n,b = map(int, input().split())
lst = []
for _ in range(n):
    data = list(map(int, input().split()))
    semi = []
    for ele in data:
        semi.append(ele % 1000)
    lst.append(semi)
memo = collections.defaultdict(list)
memo[1] = lst
def multiple(a,b):
    result = []
    for i in range(n): # 행
        semi = []
        for j in range(n): # 열
            tmp = 0
            for k in range(n):
                tmp += a[i][k] * b[k][j]
            semi.append(tmp % 1000)
        result.append(semi)
    return result

def divide_matrix(lst, b):
    if memo[b] != []:
        return memo[b]
    if b > 1:
        tmp = b//2
        multi = multiple(divide_matrix(lst, tmp), divide_matrix(lst, b-tmp))
        memo[b] = multi
        return multi
    else: # b가 1이면 결과 리턴
        return lst

result = divide_matrix(lst, b)
for res in result:
    sys.stdout.write(" ".join(map(str, res)))
    print()