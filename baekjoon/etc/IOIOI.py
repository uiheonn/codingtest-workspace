# I가 처음일 때 시작
# I는 true, O는 False로 규정하여 구분
# 번갈아가며 나오지 않는 경우가 발생 -> count 1로 초기화
# count가 limit과 일치 -> count = count - 2
n = int(input())
limit = 2*n + 1
m = int(input())
lst = input()

direction = True
count_lst = []
count = 0
for ele in lst:
    if direction and ele == 'I':
        count+=1
        direction = False
        count_lst.append(count)
    elif not direction and ele == 'O':
        if count == limit:
            count-=1
        else:
            count+=1
        direction = True
        count_lst.append(count)
    elif ele == 'I':
        count = 1
        count_lst.append(count)
    elif ele == 'O':
        count = 0
        count_lst.append(count) 

print(count_lst.count(limit))