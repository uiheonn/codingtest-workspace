from collections import Counter

def solution(participant, completion):
    answer = ""
    p_counter = Counter(participant) # 딕셔너리 형태로 정렬
    c_counter = Counter(completion) # 딕셔너리 형태로 정렬
    print(p_counter)
    print(c_counter)
    
    for i in p_counter:
        if p_counter[i] != c_counter[i]:
            answer = i
        
    return answer