n = int(input())

# 현재 숫자와 리스트의 내에 숫자의 ord의 절댓값이 1인 경우에 끌어와서 만든다

# lst = [["0","1","2","3","4","5","6","7","8","9"]]
# def concat(alphaNumber, semiLst):
#     semi = []
#     for num in semiLst:
#         tmp = abs(ord(num) - ord(alphaNumber))
#         if tmp == 1:
#             semi.append(num)
#     return semi

# def findRight(concatAvailableList, level): # concatAvailableList의 원소가 lst[level]의 원소 중 시작점인 원소를 찾아 리턴
#     semi = []
#     for num in lst[level]: # "10", "12", "21", "23", "32", "34"
#         if num[0] in concatAvailableList:
#             semi.append(num)
#     return semi

# def deleteZero(semiLst):
#     semiLstLst = semiLst.copy()
#     deleteList = []
#     for i in range(len(semiLstLst)):
#         if semiLstLst[i][0] == "0":
#             deleteList.append(semiLstLst[i])
#         else:
#             break
#     for num in deleteList:
#         semiLstLst.remove(num)
#     return semiLstLst

# for i in range(1, n): # i는 1
#     intoLst = []
#     for j in range(0,10):
#         alphaNumber = str(j) # "1"
#         concatAvailableList = concat(alphaNumber, lst[0]) # "0", "2"
#         findRightList = findRight(concatAvailableList, i-1) # ["0", "2"], 1 -> ["0", "2"] 리턴
#         for num in findRightList:
#             intoLst.append(alphaNumber + num)
#     lst.append(intoLst)

# print(lst)

# 1. 이전 배열을 통해 끝자리 수를 리턴한다 (n-1번째까지)
# 2. 9 ** n 에서 0,9의 개수를 뺀다

dp = [[0] + [1] * 9]
for i in range(1,n):
    dp.append([0] * 10)

for k in range(1, n):
    for i in range(10):
        tmp = dp[k-1][i] # 0
        if tmp == 0:
            continue
        if i == 0:
            dp[k][i+1]+=tmp
        elif i == 9:
            dp[k][i-1]+=tmp
        else:
            dp[k][i-1]+=tmp
            dp[k][i+1]+=tmp

result = dp[-1]
print(sum(result) % 1000000000)