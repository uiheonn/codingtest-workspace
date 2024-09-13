import itertools
import sys

inp = list(map(int, input().split()))

temp = list(range(1, inp[0]+1))

nPr = list(itertools.permutations(temp, inp[1]))

for ele in nPr:
    sys.stdout.write(" ".join(map(str, ele)) + "\n")