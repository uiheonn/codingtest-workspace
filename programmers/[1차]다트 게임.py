def solution(dartResult):
    answer = 0
    arr = []
    i=0
    while i<len(dartResult):
        temp=""
        if ord(dartResult[i]) >= 48 and ord(dartResult[i]) <= 57:
            j=i-1
            while ord(dartResult[j])>=48 and ord(dartResult[j])<=57:
                temp = dartResult[j] + temp
                j-=1
            tmp = int(temp + dartResult[i])
        if ord(dartResult[i]) >= 65 and ord(dartResult[i]) <= 90:
            if dartResult[i] == 'S':
                arr.append(tmp)
            if dartResult[i] == 'D':
                arr.append(tmp*tmp)
            if dartResult[i] == 'T':
                arr.append(tmp*tmp*tmp)
        if dartResult[i] == '#':
            nn = len(arr)-1
            arr[nn]*=-1
        if dartResult[i] == '*':
            nn = len(arr)
            if nn<2: # arr에 하나밖에 없다
                arr[nn-1]*=2
            else: # arr이 두개 이상이다
                arr[nn-2]*=2
                arr[nn-1]*=2
        i+=1
    
    return sum(arr)