a = int(input())

list = []

for i in range(0, a, 1):
    b = input().split()
    if(b[0] == 'push_back'):
        list.append(b[1])
    elif(b[0] == 'pop_back'):
        list.pop()
    elif(b[0] == 'get'):
        print(list[int(b[1])-1])
    elif(b[0] == 'size'):
        print(len(list))