import sys

# 1. 딕셔너리를 생성하여 배열에 넣는다. 알파벳이 key이고 value는 존재횟수로 설정한다. 초기값은 0
# 2. 이전 딕셔너리의 데이터와 현재 문자열의 알파벳을 +1한 값을 합쳐 새로운 딕셔너리를 생성하여 배열에 추가
# 3. r의 딕셔너리 value - l의 딕셔너리 value -> l과 r 사이의 알파벳의 개수가 됨


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

sys.stdout.write("\n".join(map(str, result)))