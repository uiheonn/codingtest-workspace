N = int(input())

num = []

for _ in range(N):
    line = input().split()
    if line[0] == "push_back":
        num.append(int(line[1]))
    elif line[0] == "pop_back":
        num.pop()
    elif line[0] == "size":
        print(len(num))
    elif line[0] == "get":
        print(num[int(line[1])-1])