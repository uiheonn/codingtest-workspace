import sys

# txt = input()
# n = int(input())
# lst = []
# for i in range(n):
#     t, l, s = map(str, input().split())
#     lst.append([t, int(l), int(s)])

input = sys.stdin.read
data = input().splitlines()
txt = data[0]
n = int(data[1])
lst = []
for i in range(2, n+2):
    t, l, s = data[i].split()
    lst.append([t, int(l), int(s)])

alphaLst = []
lenTxt = len(txt)
alphaDict = {}
for j in range(97, 123):
    alphaDict[chr(j)] = 0
alphaLst.append(alphaDict)

for i in range(1, lenTxt+1):
    ch = txt[i-1]
    changeNum = alphaLst[i-1][ch] + 1
    copyAlphaDict = alphaLst[i-1].copy()
    copyAlphaDict[ch] = changeNum
    alphaLst.append(copyAlphaDict)
alphaLst.pop(0)

result = []
for i in range(n):
    a, l, r = lst[i]
    # print("r : ", r, "alpha[r] : ", alphaLst[r][a])
    # print("l : ", l, "alpha[l] : ", alphaLst[l-1][a])
    # print()
    if l == 0:
        result.append(alphaLst[r][a])
    else:
        result.append(alphaLst[r][a] - alphaLst[l-1][a])

# print("recode : ", recode)
sys.stdout.write("\n".join(map(str, result)))