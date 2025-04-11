'''
알고리즘 과정
1. 정렬을 시킨다
2. 첫항부터 이동하며 limit를 넘지않는 가장 최적의 무게를 구한다(가장 뒷항부터 앞으로 이동하면서 탐색한다). 없는 경우 첫항만 보트를 통해 떠난다
3. 보트를 통해 떠난 사람들은 배열에서 삭제하고 answer를 1 추가한다
4. 또 첫항을 탐색한다
5. 배열이 모두 비었으면 종료하고 answer를 리턴한다
'''
''' 시간초과된 코드
def solution(people, limit):
    answer=0
    people = sorted(people) # [10 30 70 90]

    while len(people) != 0:
        total = people[0]
        del people[0]
        i=-1
        n=len(people)
        while len(people) != 0 and total <= limit: # 10 20 30 40
            if abs(i) > len(people):
                break
            if total+people[i] > limit:
                i-=1
                continue
            total+=people[i]
            del people[i]
        
        answer+=1

    return answer
'''
def solution(people, limit):
    answer = 0
    people.sort()  # 오름차순으로 정렬
    
    left = 0  # 왼쪽 인덱스
    right = len(people) - 1  # 오른쪽 인덱스
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1  # 왼쪽 인덱스를 오른쪽으로 이동하여 다음 사람 선택
        right -= 1  # 오른쪽 인덱스를 왼쪽으로 이동하여 다음 사람 선택
        answer += 1  # 보트 개수 증가

    return answer
