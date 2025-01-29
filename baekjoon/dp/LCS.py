a = input()
b = input()
lst = [[0 for _ in range(len(a))] for j in range(len(b))]

for i in range(len(b)):
    for j in range(len(a)):
        if a[j] == b[i]:
            if j != 0:
                lst[i][j] = lst[i-1][j-1] + 1
            else:
                lst[i][j] = 1
        else:
            lst[i][j] = max(lst[i][j-1], lst[i-1][j])
        

# for ele in lst:
#     print(ele)
print(lst[-1][-1])