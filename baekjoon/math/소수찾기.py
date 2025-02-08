n = int(input())
lst = list(map(int, input().split()))

def eratostenes(num):
    last = int(num**(1/2))+1
    data = [i for i in range(num+1)]
    for i in range(2,last):
        if data[i] == 0:
            continue
        for j in range(i*i,num+1,i):
            data[j] = 0
    return data

result = eratostenes(1000)
result[1] = 0
count=0
for ele in lst:
    if result[ele]:
        count+=1
print(count)