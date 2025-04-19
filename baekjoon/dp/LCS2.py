F = input()
S = input()

dp_lst = [[[0,""] for _ in range(len(F))] for i in range(len(S))]
for i in range(len(S)):
    for j in range(len(F)):
        if S[i] == F[j]: # 같은 문자이면
            if i == 0 or j == 0:
                dp_lst[i][j][0] = 1
                dp_lst[i][j][1] += S[i]
            else:
                dp_lst[i][j][0] = dp_lst[i-1][j-1][0] + 1
                dp_lst[i][j][1] = dp_lst[i-1][j-1][1] + S[i]
        else: # 다른 문자이면
            if i == 0 and j == 0:
                continue
            elif i == 0:
                dp_lst[i][j] = dp_lst[i][j-1]
            elif j == 0:
                dp_lst[i][j] = dp_lst[i-1][j]
            else:
                dp_lst[i][j] = max(dp_lst[i-1][j], dp_lst[i][j-1])

# for ele in dp_lst:
#     print(ele)
if dp_lst[-1][-1][0] == 0:
    print(dp_lst[-1][-1][0])
else:
    print(dp_lst[-1][-1][0])
    print(dp_lst[-1][-1][1])