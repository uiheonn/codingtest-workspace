import collections

ladder, snake = map(int, input().split())
jump_lst = []
for i in range(ladder + snake):
    jump_lst.append(list(map(int, input().split())))

visited = [False for _ in range(101)]
queue = collections.deque()
queue.append([1,0]) # 1은 현재 위치, 0은 주사위를 굴린 횟수

def isCanJump(now):
    move = now
    for i in range(len(jump_lst)):
        if jump_lst[i][0] == move:
            move = jump_lst[i][1]
            break
    
    return move


while len(queue) != 0:
    # print("queue : ", queue)
    now, dice = queue.popleft()

    if now == 100:
        print(dice)
        break

    for i in range(1, 7):
        tmp = isCanJump(now + i)
        if tmp <= 100 and not visited[tmp]:
            queue.append([tmp, dice+1])
            visited[tmp] = True