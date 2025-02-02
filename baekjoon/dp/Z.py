# 1,2,4,16,32... -> 2의 제곱 수에 규칙이 있음
# 2의 제곱 수다 -> 해당 수의 제곱
# 2의 제곱 수가 아니다 -> 해당 수보다 작으면서 가장 큰 2의 제곱 + (해당 수 - 해당 수보다 작으면서 가장 큰 2의 제곱)

n,r,c = map(int, input().split())
row = None
col = None
two_square_lst = [2**i for i in range(16)]
lst = [0]

max_rc = max(r,c)

def find(i):
    max_num = 0
    for ele in two_square_lst:
        if i > ele:
            max_num = ele
        else:
            return max_num, i-max_num

if max_rc == 0:
    col = 0
else:
    i = 1
    while max_rc != i-1:
        if i in two_square_lst:
            lst.append(i**2)
        else:
            max_tmp,tmp = find(i)
            lst.append(max_tmp**2 + lst[tmp])
        i+=1
    col = lst[-1]

print(2*lst[r] + lst[c])