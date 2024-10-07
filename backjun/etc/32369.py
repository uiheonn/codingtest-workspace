import sys

inp = list(map(int, input().split()))

n = inp[0]
chingLen = inp[1]
biLen = inp[2]

ching, bi = 1, 1
for i in range(n):
    ching += chingLen
    bi += biLen
    if ching < bi:
        ching, bi = bi, ching
    elif ching == bi:
        bi-=1

print(ching, bi)