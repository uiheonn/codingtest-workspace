def h_index(lists, h): # list : 0 5 6 7 8, h : 0,1,2,3,4
    sum = 0
    for i in range(len(lists)):
        if lists[i] >= h:
            sum+=1
    print(sum, h)
    if sum >= h:
        print("성공은 ", h)
        return True
    else:
        return False
    

def solution(citations):
    answer = 0
    lists = sorted(citations)
    n = len(lists) # 탐색할 인덱스의 마지막 값
    for i in range(n+1): # 100 100 100
        #print(i)
        if h_index(lists, i): # i : 0~2
            answer = i
        
    return answer