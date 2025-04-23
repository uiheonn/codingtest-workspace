from itertools import permutations

def permutation_case(lists):
    perms = list(permutations(lists))
    return perms
    
def solution(k, dungeons):
    answer = 0
    temp = permutation_case(dungeons) # 던전 리스트를 순열형태로 구현
    n = len(temp)
    res = k
    maxs = 0
    for i in range(n): 
        m = len(temp[i])
        for j in range(m): # temp[0] = ([80,20],[50,40],[30,10])
            if k >= temp[i][j][0]:
                answer+=1
                k = k - temp[i][j][1]
        if answer > maxs:
            maxs = answer
        answer = 0
        k = res
    
    return maxs