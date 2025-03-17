from queue import PriorityQueue
import sys

input = sys.stdin.readline
v,e = map(int, input().split())
start = int(input())
graph_lst = [[] for _ in range(v)]
for _ in range(e):
    a,b,w = map(int, input().split())
    graph_lst[a-1].append([b-1, w])
vertax_lst = [200001 for _ in range(v)]

def dijkstra(start):
    pq = PriorityQueue()
    pq.put([0,start])
    vertax_lst[start] = 0

    while not pq.empty():
        cost,s = pq.get()

        if vertax_lst[s] < cost:
            continue

        for ele in graph_lst[s]:
            if vertax_lst[ele[0]] > ele[1] + cost:
                vertax_lst[ele[0]] = ele[1] + cost
                pq.put([ele[1]+cost,ele[0]])
    return vertax_lst

temp = dijkstra(start-1)
result = []
for ele in temp:
    if ele == 200001:
        result.append("INF")
    else:
        result.append(ele)
sys.stdout.write("\n".join(map(str, result)))