d={}  
def add_score():
    global d
    k=input("請輸入科目:")
    v=input("請輸入成績:")
    d[k]=v
    print(d)
def remove_score():
    global d
    ans=input('請輸入想刪除的科目:')
    a=d.pop(ans,'哈哈哈哈沒東西')
    print(f"移除:{a}")
while True:
    for key,vlaue in d.items():
        print(f'{key}={vlaue}')
    print('1. 新增科目\n2. 刪除某個科目成績\n3. 關閉系統 ')
    ans=input('請輸入選項:')
    if ans == '1':
        add_score()
    elif ans =='2':
        remove_score()
    elif ans =='3':
        print("再見")
        break
    else:
        print('哈哈哈你打錯了')
        print('================')
