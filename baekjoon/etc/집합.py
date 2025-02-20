import sys

input = sys.stdin.readline
n = int(input().strip())

# n = int(input())
st = set()
for i in range(1, n+1):
    question = list(input().split())
    num = None
    if len(question) >= 2:
        num = question[1]
    question = question[0]

    if question == "add":
        st.add(num)
    elif question == "remove":
        st.discard(num)
    elif question == "check":
        if num in st:
            print(1)
        else:
            print(0)
    elif question == "toggle":
        if num in st:
            st.discard(num)
        else:
            st.add(num)
    elif question == "all":
        st = set(str(i) for i in range(1,21))
    else:
        st = set()