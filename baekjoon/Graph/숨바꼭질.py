import collections
n, k = map(int, input().split())

visited = [False for i in range(2 * k + 1)]
queue = collections.deque()

if n >= k:
    print(n-k)
else:
    queue.append([n,0])
    visited[n] = True

    while len(queue) != 0:
        tmp = queue.popleft()
        loc = tmp[0]
        count = tmp[1]

        if loc == k:
            print(count)
            break
    
        if loc > 0 and visited[loc-1] == False:
            queue.append([loc-1,count+1])
            visited[loc-1] = True
        if loc < k and visited[loc+1] == False:
            queue.append([loc+1, count+1])
            visited[loc+1] = True
        if 2 * loc <= 2 * k and visited[2 * loc] == False:
            queue.append([2 * loc, count+1])
            visited[2 * loc] = True