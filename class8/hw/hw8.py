a=[]

while True:
    x=input("輸入e就離開程式，請輸入想新增的資料:")
    if x =='e':
        print("再見")
        break
else:
    a.append(x)
    print(a)
