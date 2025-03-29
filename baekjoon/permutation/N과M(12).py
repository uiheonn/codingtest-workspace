import itertools
import sys

n,m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
temp = itertools.combinations_with_replacement(lst, m)

result = set()
for ele in temp:
    result.add(ele)
result = sorted(result)
for ele in result:
    sys.stdout.write(" ".join(map(str, ele)))
    print()