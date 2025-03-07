string = input()
bomb = input()

stack = []

def check(st, bm):
    count = 0
    if len(st) < len(bm):
        return False
    for i in range(1, len(bm)+1):
        if bm[-1*i] != st[-1*i]:
            break
        count+=1
    if count == len(bm):
        return True
    else:
        return False

for st in string:
    if st == bomb[-1]: # 스택 마지막 데이터가 폭발 문자열의 마지막 문자와 같다면 -> 폭발할지 확인
        stack.append(st)
        if check(stack, bomb): # 모두 일치하는 경우 -> stack에서 len(bomb)만큼 제거
            for i in range(len(bomb)):
                stack.pop()
    else:
        stack.append(st)
    # print(stack)

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(map(str, stack)))