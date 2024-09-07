total = int(input())
result = []

for i in range(total):
    stack = []
    ps = input() # (()((())))
    for j in range(len(ps)):
        if ps[j] == '(':
            stack.append('(')
        else:  # ps[j] == ')'
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
    if len(stack) == 0:
        result.append("YES")
    else:
        result.append("NO")

print("\n".join(result))