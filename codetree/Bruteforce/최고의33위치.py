n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

result = []
for i in range(n-2):
    for j in range(n-2):
        count = 0
        for k in range(i,i+3):
            for q in range(j,j+3):
                if grid[k][q] == 1:
                    count+=1
        result.append(count)
print(max(result))