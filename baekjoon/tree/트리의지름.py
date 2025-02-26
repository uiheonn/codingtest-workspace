import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
n = int(input())
graph_lst = [[] for _ in range(n)]
if n == 1:
    print(0)
else:
    for _ in range(n-1):
        s,d,cost = map(int, input().split())
        graph_lst[s-1].append([d-1,cost])

    # print(graph_lst)

    result = []
    def find_cost(start, prior):
        if start == prior:
            return 0
        tmp = graph_lst[prior]
        for ele in tmp:
            if ele[0] == start:
                return ele[1]

    def recursive(start, prior): # 현재 노드, 부모 노드
        lst = graph_lst[start] # [[1,3], [2,2], [5,4]]
        if len(lst) >= 2: # 자식이 2개면 지름과 간선의 역할을 할 수 있다 -> 루트 빼고
            semi = []
            for ele in lst:
                semi.append(recursive(ele[0], start))
            first = max(semi)
            semi.remove(max(semi))
            second = max(semi)
            if start == 0:
                result.append(first + second)
            else:
                result.append(first+second) # start 노드에서 최대 지름
                return max(first,second) + find_cost(start, prior) # start 노드의 두 갈래의 자식 중 더 길이가 긴 값
        elif len(lst) == 1:
            tmp = recursive(lst[0][0], start)
            result.append(tmp)
            return tmp + find_cost(start, prior)
        else: # 자식이 없는 경우 -> 밑단 노드인 경우
            return find_cost(start, prior)
    recursive(0,0)
    print(max(result))