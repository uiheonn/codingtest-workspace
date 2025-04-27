N = int(input())
value = []

for _ in range(N):
    line = input().split()
    if line[0] == "push":
        value.append(int(line[1]))
    elif line[0] == "pop":
        print(value.pop())
    elif line[0] == "size":
        print(len(value))
    elif line[0] == "empty":
        if len(value):
            print(0)
        else:
            print(1)
    else:
        print(value[-1])