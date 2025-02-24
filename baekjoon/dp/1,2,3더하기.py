t = int(input())

for _ in range(t):
    n = int(input())

    def dp(n):
        if n >= 3:
            return dp(n-1)+dp(n-2)+dp(n-3)
        elif n == 2:
            return dp(n-1)+dp(n-2)
        elif n == 1:
            return dp(n-1)
        else:
            return 1
    
    print(dp(n))