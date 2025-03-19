import collections
import sys

input = sys.stdin.readline
n,e = map(int, input().split())
graph_lst = [[] for _ in range(n)]
for _ in range(e):
    a,b,cost = map(int, input().split())
    graph_lst[a-1].append([b-1,cost])
    graph_lst[b-1].append([a-1,cost])
must_a,must_b = map(int, input().split())
must_a-=1
must_b-=1
def dickstra(start, not_in):
    vertax_list = [200000001 for _ in range(n)]
    queue = collections.deque()
    queue.append([start,0])
    vertax_list[start] = 0
    while len(queue) != 0:
        vertax, cost = queue.popleft()
        if vertax_list[vertax] != cost:
            continue

        for i in range(len(graph_lst[vertax])):
            l,r = graph_lst[vertax][i]
            if vertax_list[l] > cost + r:
                vertax_list[l] = cost + r
                queue.append([l, vertax_list[l]])
    # print(vertax_list)
    return vertax_list

a = dickstra(must_a, must_b)
b = dickstra(must_b, must_a)
common = a[must_b]
mx = min(common + a[0] + b[-1], common + a[-1] + b[0])
if mx >= 200000001:
    print(-1)
else:
    print(mx)