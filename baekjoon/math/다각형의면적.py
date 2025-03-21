import sys

input = sys.stdin.readline
n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

# print(lst)

def diterminant(a,b):
    return a[0] * b[1] - a[1] * b[0]

result = 0
for i in range(n-1):
    result += diterminant(lst[i], lst[i+1])
result += diterminant(lst[-1], lst[0])
print(round(abs(result)/2,1))