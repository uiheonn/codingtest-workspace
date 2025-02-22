# LIS 알고리즘과 유사
# 동일하거나 탕후루 종류가 2개 이하면 +1
# 탕후루 종류가 3개 이상이 되면 "현재 위치 직전 탕후루 종류의 시작점"부터 현재 위치까지를 count로 초기화하고 시작
# 이런식으로 count list를 만들고 최대값을 리턴

n = int(input())
lst = list(map(int, input().split()))

check = dict()
dp_lst = []
count = 0
for i in range(len(lst)):
    if lst[i] in check.keys():
        count+=1
        check[lst[i]] = i
        dp_lst.append(count)
    else:
        if len(check) < 2:
            count+=1
            check[lst[i]] = i
            dp_lst.append(count)
        else:
            temp = list(check.keys())
            max_key, min_key = temp[0], temp[1]
            if check[max_key] < check[min_key]:
                max_key, min_key = min_key, max_key
            count = check[max_key] - check[min_key] + 1
            dp_lst.append(count)
            check[lst[i]] = i
            check.pop(min_key)
print(max(dp_lst))