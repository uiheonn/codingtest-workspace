import sys

r = int(input())
c = 2 * r

tmp = ["*", "* *", "*****"]

while len(tmp) != r:
    semi = []
    for i in range(len(tmp)-1,-1,-1): # 2,1,0, ...
        index = abs(i - len(tmp) + 1)
        side = tmp[index]
        center = len(tmp[i])
        string = side
        for i in range(center):
            string += " "
        string+= side
        semi.append(string)
    for ele in semi:
        tmp.append(ele)

def make_string(string,col):
    res = ""
    index = (col-len(string))//2 # string이 시작하는 인덱스
    for i in range(0,index):
        res+=" "
    res+=string
    for i in range(len(res),col):
        res+=" "
    return res

result = []
for ele in tmp:
    result.append(make_string(ele,c)) # "* *"

sys.stdout.write("\n".join(map(str, result)))