n = int(input())

lst = [1,3]

if n < 3:
    print(lst[n-1])
else:
    while len(lst) != n:
        lst.append((2*lst[-2] + lst[-1]) % 10007)
    print(lst[-1])