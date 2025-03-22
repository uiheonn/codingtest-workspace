import collections
import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
N,U,Q = map(int, input().split())
graph_lst = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int, input().split())
    graph_lst[a-1].append(b-1)
    graph_lst[b-1].append(a-1)

# print(graph_lst)

tree_lst = [[] for _ in range(N)]
queue = collections.deque()
queue.append(U-1)
visited = [False for _ in range(N)]
while len(queue) != 0:
    node = queue.popleft()
    for ele in graph_lst[node]:
        if not visited[ele]:
            tree_lst[node].append(ele)
            queue.append(ele)
    visited[node] = True

# print(tree_lst)
dic = collections.defaultdict(int)
def recursive(start):
    if dic[start]:
        return dic[start]

    if len(tree_lst[start]) == 0:
        dic[start] = 1
        return 1
    
    count = 1
    for ele in tree_lst[start]:
        count += recursive(ele)
    dic[start] = count
    return count

result = []
for _ in range(Q):
    s = int(input())
    result.append(recursive(s-1))

# print(result)
sys.stdout.write("\n".join(map(str, result)))