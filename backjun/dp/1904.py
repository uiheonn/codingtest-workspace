inp = int(input())

memo = [1, 1]
def fibo(n):
    l = len(memo)
    for i in range(l, n+1):
        memo.append((memo[i-1] + memo[i-2]) % 15746)
    return memo[n]

print(f"{fibo(inp)}")