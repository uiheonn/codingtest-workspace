t = int(input())

lst = [[0,0,1], [1,1,0]]

number_lst = []
for i in range(1,t+1):
    number_lst.append(int(input()))

max_data = max(number_lst)

def fibonacci(n):
    if len(lst) > n:
        return lst[n]
    else:
        fi1 = fibonacci(n-1)
        fi2 = fibonacci(n-2)
        # print("lst : ", lst)
        # print("n : ", n)
        # print("fi1 : ", fi1)
        # print("fi2 : ", fi2)
        sum_data = fi1[0] + fi2[0]
        sum_one = fi1[1] + fi2[1]
        sum_zero = fi1[2] + fi2[2]
        tmp = [sum_data, sum_one, sum_zero]
        lst.append(tmp)
        return tmp

fibonacci(max_data)

for ele in number_lst:
    print(lst[ele][2], lst[ele][1])