import sys
from collections import defaultdict

input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())

dic = defaultdict(int)

for i in range(1, n + 1):
    text = data[i]
    if len(text) >= m:
        dic[text] += 1

res = sorted(dic.keys(), key=lambda x: (-dic[x], -len(x), x))

sys.stdout.write("\n".join(res) + "\n")