import sys

input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
tree = list(map(int, data[1].split()))

# n, m = map(int, input().split()) # 5 20
# tree = list(map(int, input().split())) # 4 42 40 26 46

tree.sort()

def maxTreeHeight(tree, n, m):
    left = 1
    right = tree[-1]
    maxHeight = 0
    while left <= right:
        total = 0
        mid = (left+right)//2 # 25
        for i in range(n):
            slice = tree[i] - mid
            if slice > 0:
                total+=slice
        if total < m: # 너무 절단 높이가 높다 -> 절단 높이를 낮추기 -> mid를 낮추기 
            right = mid - 1
        elif total > m: # 너무 절단 높이가 낮다 -> 절단 높이를 높이기 -> mid를 높이기
            if mid > maxHeight:
                maxHeight = mid
            left = mid + 1
        else: # 절단 높이가 딱 맞게 나무를 잘랐다 -> maxHeight 수정 + 높이를 올린다
            maxHeight = mid
            break
            #left = mid + 1
    return maxHeight

print(maxTreeHeight(tree, n, m))