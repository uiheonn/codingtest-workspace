import sys

input = sys.stdin.read
data = input().splitlines()

total = int(data[0])
lst = []
result = []

for i in range(1, total + 1):
    inputNum = data[i].split()
    if inputNum[0] == '1':
        lst.append(inputNum[1])
    elif inputNum[0] == '2':
        if lst:
            result.append(lst.pop())
        else:
            result.append(-1)
    elif inputNum[0] == '3':
        result.append(len(lst))
    elif inputNum[0] == '4':
        if lst:
            result.append(0)
        else:
            result.append(1)
    elif inputNum[0] == '5':
        if lst:
            result.append(lst[-1])
        else:
            result.append(-1)

sys.stdout.write("\n".join(map(str, result)) + "\n")