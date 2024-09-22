import sys

input = sys.stdin.read
data = input().splitlines()
n = int(data[0])

result = []
for i in range(1, n+1):
    p = [1,1,1,2,2]
    inp = int(data[i])
    l = len(p)
    if inp < l:
        result.append(p[inp - 1])
    else:
        for j in range(5, inp):
            p.append(p[j - 1] + p[j - 5])
        result.append(p[inp - 1])


sys.stdout.write("\n".join(map(str, result)) + "\n")