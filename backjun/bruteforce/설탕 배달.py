# 1.5으로 나누어지나? yes면 -5, no면 -3
# 2. while 0보다 작을때까지

n = int(input()) # 18

tmp=0
while n > 0:
    if n % 5 == 0:
        n-=5
        tmp+=1
    else:
        n-=3
        tmp+=1

if n!=0:
    tmp=-1
    
print(tmp)