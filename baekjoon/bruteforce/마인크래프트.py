# 가장 높은 값의 개수 * 2 + 한칸 깎은 후에 땅을 덮는 시간 vs 나머지 땅을 가장 높은 값으로 덮을 경우의 시간
# 덮을만큼의 인벤토리가 없다 -> 닥전
# 딕셔너리로 효율성 개선

r,c,b = map(int, input().split())
dic = dict()
for _ in range(r):
    tmp = list(map(int, input().split()))
    for ele in tmp:
        if dic.get(ele):
            dic[ele]+=1
        else:
            dic[ele]=1

time = 0
while len(dic.keys()) != 1:
    max_height = max(dic.keys())

    semi_dic = dic.copy()
    semi_dic[max_height-1] = semi_dic.get(max_height-1,0) + semi_dic[max_height]
    delete_sum = semi_dic[max_height] * 2
    semi_dic.pop(max_height)
    for ele in semi_dic.keys():
        if ele != max_height-1:
            delete_sum = delete_sum + (max_height-1 - ele) * semi_dic[ele]
    semi_dic.clear()

    put_sum = 0
    for ele in dic.keys():
        put_sum = put_sum + (max_height - ele) * dic[ele]

    inbentory = True
    if put_sum > b:
        inbentory = False
    
    if delete_sum < put_sum or not inbentory: # 땅을 파는게 더 이득인 경우 or 인벤토리가 부족한 경우 -> 땅파기
        dic[max_height-1] = dic.get(max_height-1,0) + dic[max_height]
        b+=dic[max_height]
        time+=dic[max_height] * 2
        dic.pop(max_height)
    else: # 땅 쌓기
        for ele in dic.keys():
            if ele != max_height:
                dic[max_height] += dic[ele]
        key_lst = list(dic.keys())
        for ele in key_lst:
            if ele != max_height:
                dic.pop(ele)
        b-=put_sum
        time+=put_sum
        
result = list(dic.keys())
result.sort(reverse=True)
print(time, result[0])