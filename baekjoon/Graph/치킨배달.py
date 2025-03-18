import sys
import itertools
import collections


input = sys.stdin.readline
n,m = map(int, input().split())
graph = []
chicken_location = []
house_location = collections.defaultdict(int)
for i in range(n):
    semi_lst = list(map(int, input().split()))
    for j in range(len(semi_lst)):
        if semi_lst[j] == 2:
            chicken_location.append([i,j])
        elif semi_lst[j] == 1:
            house_location[(i,j)] = 100001
    graph.append(semi_lst)

chicken_combinations = itertools.combinations(chicken_location, m)
chicken_combination_lists = []
for ele in chicken_combinations:
    chicken_combination_lists.append(list(ele))

result = []
for best_chick_loc in chicken_combination_lists:
    now_house_location = house_location.copy()
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                for ele in best_chick_loc:
                    chicken_x, chicken_y = ele
                    distance = abs(i - chicken_x) + abs(j - chicken_y)
                    if now_house_location[(i,j)] > distance:
                        now_house_location[(i,j)] = distance

    result.append(sum(now_house_location.values()))
print(min(result))