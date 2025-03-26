import itertools
import sys

n,m = map(int, input().split()) # 3 1
lst = [i for i in range(1,n+1)]

temp = itertools.combinations_with_replacement(lst, m)

result = []
for ele in temp:
    tmp = list(ele)
    result.append(tmp)

# sys.stdout.write("\n".join(map(str, " ".join(map(str, result)))))
for ele in result:
    sys.stdout.write(" ".join(map(str, ele)))
    print()