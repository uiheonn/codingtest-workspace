n = int(input())
tmp_a,tmp_b,tmp_c = map(int,input().split())
mx_a,mx_b,mx_c = tmp_a,tmp_b,tmp_c
tmpn_a,tmpn_b,tmpn_c = tmp_a,tmp_b,tmp_c
mn_a,mn_b,mn_c = tmpn_a,tmpn_b,tmpn_c

for _ in range(1,n):
    a,b,c = map(int, input().split())
    mx_a=max(tmp_a,tmp_b)+a
    mx_b=max(tmp_b,tmp_a,tmp_c)+b
    mx_c=max(tmp_c,tmp_b)+c
    
    mn_a=min(tmpn_a,tmpn_b)+a
    mn_b=min(tmpn_a,tmpn_b,tmpn_c)+b
    mn_c=min(tmpn_b,tmpn_c)+c
    
    tmp_a = mx_a
    tmp_b = mx_b
    tmp_c = mx_c
    tmpn_a = mn_a
    tmpn_b = mn_b
    tmpn_c = mn_c

print(max(mx_a, mx_b, mx_c), min(mn_a,mn_b,mn_c))