import collections
import sys

input = sys.stdin.readline
n,m = map(int, input().split()) # 사람 수, 간선의 수
true = list(map(int, input().split())) # 진실을 아는 사람의 수, 진실을 하는 사람의 번호

graph_lst = [[] for _ in range(n)]
lst = []
for _ in range(m):
    lst.append(list(map(int, input().split())))

for ele in lst:
    if len(ele) >= 3:
        for i in range(1, len(ele)-1): # 1~2
            if ele[i+1]-1 not in graph_lst[ele[i]-1]:
                graph_lst[ele[i]-1].append(ele[i+1]-1)
            if ele[i]-1 not in graph_lst[ele[i+1]-1]:
                graph_lst[ele[i+1]-1].append(ele[i]-1)
#print(graph_lst)

visited = [False for _ in range(n)]
def bfs(start):
    if visited[start]:
        return
    queue = collections.deque()
    queue.append(start)
    visited[start] = True
    while len(queue) != 0:
        tmp = queue.popleft() # 1

        for ele in graph_lst[tmp]:
            if not visited[ele]:
                queue.append(ele)
                visited[ele] = True

true_n = true.pop(0)
for i in range(true_n):
    start = true[i]-1
    bfs(start)

#print("visited : ", visited)

count = 0
for ele in lst:
    right = True
    for tmp in ele[1:]:
        if visited[tmp-1]:
            right = False
            break
    if right:
        count+=1
print(count)