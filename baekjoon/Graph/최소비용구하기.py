# 다익스트라로 구현
# distance 배열 필요
# 1. pq에 시작 노드 추가
# 2. 최상단의 데이터를 빼면서 다익스트라 수행
# 3. 공집합이 되면 반복문 종료
from queue import PriorityQueue

n = int(input())
m = int(input())
distance = [1000000001 for _ in range(n)]
graph_lst = [[] for _ in range(n)]
pq = PriorityQueue()
for _ in range(m):
    a,b,cost = map(int, input().split())
    if a == b:
        graph_lst[a-1].append([b-1,0])
    else:
        graph_lst[a-1].append([b-1,cost])

start, end = map(int, input().split())
pq.put([start-1,0])
distance[start-1] = 0

# for ele in graph_lst:
#     print(ele)
# count=0
while not pq.empty():
    post, cost = pq.get()
    if distance[post] != cost:
        continue
    # print("현재 노드 : ", post)
    # print("현재 비용 : ", cost)
    # print("distance : ", distance)
    # print()
    # count+=1

    for i in range(len(graph_lst[post])):
        l,r = graph_lst[post][i]
        if distance[l] > cost + r:
            distance[l] = cost + r
            pq.put([l,distance[l]])

print(distance)
# print("호출 횟수 : ", count)