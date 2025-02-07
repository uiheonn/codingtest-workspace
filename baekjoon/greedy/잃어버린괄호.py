data = input()
lst = []
count = 0
for i in range(len(data)):
    if data[i] == '-':
        lst.append(int(data[count:i]))
        lst.append('-')
        count = i+1
    elif data[i] == '+':
        lst.append(int(data[count:i]))
        lst.append('+')
        count = i+1
lst.append(int(data[count:]))

while len(lst) != 1:
    index,a,b = None,None,None
    if '+' in lst:
        index = lst.index('+')
    if index:
        a,b = lst[index-1], lst[index+1]
        lst.insert(index+2, a+b)
        for _ in range(3):
            lst.pop(index-1)

    index = None
    if '+' not in lst and '-' in lst:
        index = lst.index('-')
    if index:
        a,b = lst[index-1], lst[index+1]
        lst.insert(index+2, a-b)
        for _ in range(3):
            lst.pop(index-1)
print(lst[0])