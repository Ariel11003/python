l=[]
f = ["田田花釀雞", "米圓塔", "江湖百味", "杏仁豆腐"]
while True:
    print(f"目前已點的餐:{l}")
    print('1. 新增餐點\n2. 移除餐點\n3. 提交菜單')
    ans=input('請輸入功能選項:')
    if ans == '1':
        print("1.田田花釀雞\n2.米圓塔\n3.江湖百味\n4.杏仁豆腐\n")
        o=int(input('請輸入餐點編號:'))
        l.append(f[o-1])
    elif ans =='2':
        ans=input('請輸入想移除的餐點完整名稱:')
        while ans in l:
            l.remove(ans)
    elif ans =='3':
        k=[]
        for i in l:
            if i in k:
                continue
            else:
                k.append(i)
        for i in k:
            print(f'{i}有{l.count(i)}個')
        break
    else:
        print('哈哈哈你打錯了')







#     if ans =='e':
#         break
#     else:
#         l.append(ans)
#         print(l)
        
# while True:
#     ans=input('del(e=exit):')
#     if ans == 'e':
#         break
#     else:
#         while ans in l:
#             l.remove('a')
#     print(l)

# k=[]
# for i in l:
#     if i in k:
#         continue
#     else:
#         k.append(i)
# for i in k:
#     print(f'{i}有{l.count(i)}個')