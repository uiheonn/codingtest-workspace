import sys
# 1. n-1개의 원을 2번째에 옮긴다.
# 2. n의 원을 3번째에 옮긴다.
# 3. n-1개의 원을 3번째에 옮긴다.

# hanoi(from , to, num)
# from -> from, to가 아닌 위치로 num-1개를 옮긴다
# from -> to로 num원반을 옮긴다
# from, to가 아닌 위치 -> to로 num-1개를 옮긴다

inp = int(input()) # 3
result = []

def notFromOrTo(fr, to):
    les = [1, 2, 3]
    for num in les:
        if num != fr and num != to:
            return num
    

def hanoi(fr, to, num): # from에서 to까지
    frto = str(fr) + " " + str(to)
    if num == 1:
        result.append(frto)
    else:
        notFromOrToNum = notFromOrTo(fr, to)
        hanoi(fr, notFromOrToNum, num-1)
        result.append(frto)
        hanoi(notFromOrToNum, to, num-1)

print(2 ** inp - 1)
hanoi(1, 3, inp)

sys.stdout.write("\n".join(result) + "\n")