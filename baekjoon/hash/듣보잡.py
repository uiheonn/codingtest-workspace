# 3 4
# ohhenrie
# charlie
# baesangwook
# obama
# baesangwook
# ohhenrie
# clinton
import sys

input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
temp = dict()

for i in range(1, n+m+1):
    tmp = data[i]
    if temp.get(tmp):
        temp[tmp] += 1
    else:
        temp[tmp] = 1

result = []
for ele in temp:
    if temp[ele] == 2:
        result.append(ele)

result.sort()

print(len(result))
sys.stdout.write("\n".join(map(str, result)))