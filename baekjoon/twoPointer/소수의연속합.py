n = int(input())

# 소수 구하는 법 : 에라토스테네스의 체
# 투포인터로 같은 수를 찾는다
# 1. n > sum -> r++
# 2. n == sum -> l++, count++
# 3. n < sum -> l++

def prime_numbers(n):
    arr = [i for i in range(n+1)]
    nn = int(n**(1/2))
    for i in range(2,nn+1):
        if arr[i] == 0:
            continue
        for j in range(i*i, n+1, i):
            arr[j] = 0
    return [ele for ele in arr[2:] if ele]

lst = prime_numbers(n)
print(lst)

l,r = 0,0
lst_n = len(lst)
if lst_n != 0:
    summ = lst[0]
count=0
while r < lst_n:
    if n > summ: # 더 추가해야한다면
        if r == lst_n-1:
            break
        r+=1
        summ+=lst[r]
    elif n < summ: # 빼야한다면
        summ-=lst[l]
        l+=1
    else: # 동일하다면
        # print("equal data : ", lst[l:r+1])
        summ-=lst[l]
        l+=1
        count+=1
print(count)