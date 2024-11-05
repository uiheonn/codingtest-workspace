# import sys

# input = sys.stdin.read
# data = input().splitlines()
# n, m = map(int, data[0].split())
# lst = list(map(int, data[1].split()))

# output = []
# for a in range(m):
#     i, j = map(int, data[a + 2].split())
#     output.append(f"{sum(lst[i-1 : j])}\n")

# sys.stdout.write("".join(output))

n, m = map(int, input().split()) # 5, 3
lst = list(map(int, input().split())) # [5, 4, 3, 2, 1]

prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + lst[i - 1]

for i in range(m):
    i, j = map(int, input().split()) # 1 3, 2, 4
    print(prefix[j] - prefix[i - 1])