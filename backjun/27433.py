inp = int(input())

def ft(num): # num = 5
    if num == 0:
        return 1
    return num * ft(num-1)

print(ft(inp))