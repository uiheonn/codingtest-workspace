a = int(input())

list = []

for i in range(0, a, 1):
    b = input().split()
    if b[0] == 'push_back':
        list.append(b[1])
    elif b[0] == 'push_front':
        list.insert(0, b[1])
    elif b[0] == 'pop_front':
        print(list.pop(0))
    elif b[0] == 'pop_back':
        print(list.pop())
    elif b[0] == 'size':
        print(len(list))
    elif b[0] == 'empty':
        if len(list) == 0:
            print(1)
        else:
            print(0)
    elif b[0] == 'front':
        print(list[0])
    else:
        print(list[-1])