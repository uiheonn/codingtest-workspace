import sys
input = sys.stdin.read
output = sys.stdout.write

inp = int(input().strip())

fibonacciNum = 0

f = [0] * (inp + 1)
def fibonacci(n):
    global f, fibonacciNum
    if n >= 1:
        f[1] = 1
    if n >= 2:
        f[2] = 1
    for i in range(3, n + 1):
        fibonacciNum += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]

data = fibonacci(inp)

output(f"{data} {fibonacciNum}\n")