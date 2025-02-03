n = int(input())

lst = [1,2]

def fibonacci(n):
    if n <= len(lst)-1:
        return lst[n]
    tmp = (fibonacci(n-1)+fibonacci(n-2)) % 10007
    lst.append(tmp)
    return tmp

fibonacci(n-1)
print(lst[n-1])