import sys
import collections

input = sys.stdin.readline
n,m,r = map(int, input().split())
n_value = list(map(int, input().split()))
graph_lst = [[] for _ in range(n)]
graph_value = collections.defaultdict(tuple)
for _ in range(r):
    a,b,c = map(int, input().split())
    graph_lst[a-1].append(b-1)
    graph_lst[b-1].append(a-1)
    graph_value[(a-1,b-1)] = c
    graph_value[(b-1,a-1)] = c

def dijkstra(start):
    dig_list = [10000001 for _ in range(n)]
    dig_list[start] = n_value[start]
    queue = collections.deque()
    queue.append([start, 0])
    while len(queue) != 0:
        region, distance = queue.popleft()

        for ele in graph_lst[region]:
            if graph_value[(region,ele)] + distance <= m:
                queue.append([ele, graph_value[(region,ele)] + distance])
                dig_list[ele] = n_value[ele]
    total = 0
    for d in dig_list:
        if d != 10000001:
            total+=d
    return total


max_cost = 0
for i in range(n):
    result = dijkstra(i)
    if result > max_cost:
        max_cost = result
print(max_cost)