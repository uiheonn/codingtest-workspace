import sys

input = sys.stdin.read
data = input().splitlines()
n = int(data[0])
lst = list(map(int, data[1].split()))

# n = int(input())
# lst = list(map(int, input().split()))

set1 = set()
for ele in lst:
    set1.add(ele)

sorted_lst = sorted(list(set1))
# print("sorted_lst : ", sorted_lst)
count = 0
dic = dict()
for ele in sorted_lst:
    dic[ele] = count
    count+=1

result = []
for ele in lst:
    result.append(dic[ele])

sys.stdout.write(" ".join(map(str, result)))