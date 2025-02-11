import collections

t = int(input())
result = []
for _ in range(t):
    rd = input()
    p = int(input())
    l = input()[1:-1]
    lst = []
    if len(l) != 0:
        lst = list(map(int, l.split(",")))
    queue = collections.deque(lst)

    pointer = 0
    right = True
    for i in rd:
        if i == 'R': # R인 경우
            if pointer == 0:
                pointer = len(queue)-1
            else:
                pointer = 0
        else: # D인 경우
            if len(queue) == 0:
                right = False
                break
            if pointer == 0:
                queue.popleft()
            else:
                queue.pop()
                pointer-=1
    
    if right:
        if pointer == 0:
            result.append(list(queue))
        else:
            queue.reverse()
            result.append(list(queue))
    else:
        result.append("error")

for ele in result:
    if ele == "error":
        print(ele)
    elif len(ele) == 0:
        print(ele)
    else:
        st = "["
        for i in range(len(ele)):
            if i != len(ele) - 1:
                st+=str(ele[i])
                st+=","
            else:
                st+=str(ele[i])
        st+="]"
        print(st)