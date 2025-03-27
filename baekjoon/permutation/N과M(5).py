import itertools
import sys

n,m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
temp = itertools.permutations(lst, m)

for ele in temp:
    sys.stdout.write(" ".join(map(str, ele)))
    print()