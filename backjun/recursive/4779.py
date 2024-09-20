import sys

input = sys.stdin.read
data = map(int, input().splitlines())

def recursive(tmp): # ---------
    length = len(tmp)//3
    front = tmp[:length]
    mid = " " * length
    back = tmp[2*length:]

    if len(tmp) != 1:
        front = recursive(front) # ---
        back = recursive(back) # ---
    else:
        return tmp

    return front + mid + back

result = []
for i in data:
    tmp = 3 ** i * "-"
    result.append(recursive(tmp))

sys.stdout.write("\n".join(result) + "\n")