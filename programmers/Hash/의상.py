'''
옷의 종류가 3가지고 옷의 개수가 a,b,c라면
(1+a)(1+b)(1+c) - 1
옷의 종류가 2가지고 ''
(1+a)(1+b) - 1
'''
from collections import Counter

def solution(clothes):
    answer = 0
    clothes = [sublist[1:] for sublist in clothes]
    clothes = [sublist[0] for sublist in clothes]
    n = len(clothes)
    print(clothes)
    tmplist = []
    counter = Counter(clothes)
    most_common_elements = counter.most_common()
    m = len(most_common_elements)
    print(most_common_elements)
    for j in range(m):
        tmplist.append(most_common_elements[j][1])
    print("tmplist:", tmplist)
    totalsum = 1
    for i in range(len(tmplist)):
        totalsum*=(1+tmplist[i])
    
    return totalsum-1