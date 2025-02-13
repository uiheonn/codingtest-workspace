# 최대 힙, 최소 힙 두개를 생성
# 삭제할 때 deletes 리스트를 확인하고 삭제할 원소와 동일한 값이 상대의 리스트에 있다면 deletes 리스트와 함께 삭제
# deletes 리스트와 동일한 값이 없을 때까지 반복
# 반복을 마친 뒤 삭제 연산 수행 -> 자신의 deletes 리스트에 추가
# 최대 힙, 최소 힙에 남은 데이터 중 둘 다 존재하는 값들이 최종적으로 남는 데이터임

import sys
import heapq
import collections

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    max_heap = []
    min_heap = []
    max_dic = dict()
    min_dic = dict()
    for i in range(n):
        alpha, num = map(str, input().split())
        num = int(num)
        if alpha == 'I':
            heapq.heappush(max_heap, -1 * num)
            heapq.heappush(min_heap, num)
        else:
            if num == 1:
                # heap의 가장 우선순위 데이터를 확인
                # 데이터가 min_dic의 key 중 존재한다면 그냥 제거
                # key 중 존재하지 않는다면 제거
                # 제거한 데이터는 max_dic에 추가
                if len(max_heap) == 0:
                    continue
                tmp = max_heap[0] * -1
                while True:
                    if len(max_heap) == 0:
                        break
                    if tmp in min_dic.keys():
                        min_dic[tmp] -= 1
                        heapq.heappop(max_heap)
                        if min_dic[tmp] == 0:
                            min_dic.pop(tmp)
                        if len(max_heap) != 0:
                            tmp = max_heap[0] * -1
                    else:
                        break
                if len(max_heap) != 0:
                    temp = heapq.heappop(max_heap) * -1
                    if max_dic.get(temp):
                        max_dic[temp]+=1
                    else:
                        max_dic[temp]=1
            else:
                if len(min_heap) == 0:
                    continue
                tmp = min_heap[0]
                while True:
                    if len(min_heap) == 0:
                        break
                    if tmp in max_dic.keys():
                        max_dic[tmp] -= 1
                        heapq.heappop(min_heap)
                        if max_dic[tmp] == 0:
                            max_dic.pop(tmp)
                        if len(min_heap) != 0:
                            tmp = min_heap[0]
                    else:
                        break
                if len(min_heap) != 0:
                    temp = heapq.heappop(min_heap)
                    if min_dic.get(temp):
                        min_dic[temp]+=1
                    else:
                        min_dic[temp]=1

    real_max_heap = []
    result = []
    for ele in max_heap:
        real_max_heap.append(ele * -1)
    st1 = set(real_max_heap)
    st2 = set(min_heap)
    res = collections.Counter(list(st1)) + collections.Counter(list(st2))
    for ele in res.keys():
        if res[ele] == 2:
            result.append(ele)
    if len(result):
        print(max(result), min(result))
    else:
        print("EMPTY")