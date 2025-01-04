import sys

sys.setrecursionlimit(10 ** 9)

# n,m,r = map(int, input().split())
# lst = []
# for i in range(m):
#     a,b = map(int, input().split())
#     lst.append([a,b])

input = sys.stdin.read
data = input().splitlines()
n,m,r = map(int, data[0].split())
lst = []
for i in range(1,m+1):
    a,b = map(int, data[i].split())
    lst.append([a,b])

visited = [False] * (n+1) # 정점을 방문했는지 확인하는 배열
stack = [] # 스택을 통해 dfs 수행
result = []

def makeCostLst(start):
    costLst = []
    for ele in lst:
        if start in ele:
            #if ele[0] == start and visited[ele[1]] != True and ele[1] not in stack:
            if ele[0] == start and visited[ele[1]] != True:
                costLst.append(ele[1])
            #elif ele[1] == start and visited[ele[0]] != True and ele[0] not in stack:
            elif ele[1] == start and visited[ele[0]] != True:
                costLst.append(ele[0])
    costLst.sort(reverse=True)

    for ele in costLst:
        stack.append(ele)

def dfs_mat(start):
    if visited[start] == True:
        return

    makeCostLst(start) # start 정점과 연결되어있는 정점의 집합. 내림차순 정렬하여 스택에 추가
    visited[start] = True # stack에 이미 방문한 정점은 다시 가지 않도록 True로 업데이트
    result.append(start)
    # print("stack : ", stack)
    # print()
    # for i in range(len(stack)-1, -1, -1):
    #     dfs_mat(stack[i])
    while stack != []:
        st = stack.pop()
        dfs_mat(st)

dfs_mat(r)

resultDict = {}
for i in range(0,len(result)):
    resultDict[result[i]] = i+1

total = []
for i in range(1, n+1):
    tmp = resultDict.get(i)
    if tmp:
        total.append(tmp)
    else:
        total.append(0)

sys.stdout.write("\n".join(map(str, total)))