n = int(input())

def printStart(i):
    if i!=0:
        print("* ", end="")
        return printStart(i-1)
    else:
        return

for i in range(n,0,-1):
    printStart(i)
    if i != 1:
        print("")
    
for i in range(0,n+1,1):
    printStart(i)
    if i != n:
        print("")
    