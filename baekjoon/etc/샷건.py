lis = []
for _ in range(4):
    inp = input()
    lis.append(inp)

key = input()

sortList = [0] * 40

tmp = 0
for i in range(9):
    for ele in lis:
        for j in range(10):
            if key[i] == ele[j]:
                sortList[tmp] = ele[j]
            else:
                tmp+=1
    tmp = 0

temp = 0
for i in range(40):
    if sortList[i] != 0:
        temp+=1
    if temp == 5:
        print(sortList[i])
        break