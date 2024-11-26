import sys

input = sys.stdin.read
data = input().splitlines()
n, k = map(int, data[0].split())
lst = []
for i in range(1,n+1):
    lst.append(int(data[i]))

#n, k = map(int, input().split())
#lst = []
#for i in range(n):
#    lst.append(int(input()))

maxData = max(lst)

def binarySearch(arr, size, maxData): # [2147483647,2147483647,...], 
    left = 1
    right = maxData # 1
    maxLancable = 0
    while left <= right: # 3 < 3
        mid = (left + right)//2 # 0
        count = 0
        if mid == 0:
            return 0
        for i in range(len(arr)):
            count+=arr[i]//mid
        if count > size:
            maxLancable = mid
            left = mid + 1 # left = 3
        elif count < size:
            right = mid - 1
        else:
            maxLancable = mid
            left = mid + 1
    return maxLancable    


print(binarySearch(lst, k, maxData)) 