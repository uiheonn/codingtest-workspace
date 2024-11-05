import sys

input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
lst = list(map(int, data[1].split()))

temp = [0] * (n + 1)
for i in range(1, n + 1):
    temp[i] = temp[i-1] + lst[i-1]

output = []
for a in range(m):
    i, j = map(int, data[a + 2].split())
    output.append(f"{temp[j] - temp[i-1]}\n")

sys.stdout.write("".join(output))