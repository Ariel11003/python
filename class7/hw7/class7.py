import random
vvvvv=random.randint(1,100)
a=1
b=100

while True:
    ppt=int(input(f"輸入{a}~{b}:"))
    if vvvvv<ppt:
        print("再小一點")
        if  a< ppt < b:
            b=ppt
    elif vvvvv>ppt:
        print("再大一點")
        if a<ppt<b:
            a=ppt
    else:
        print('恭喜')
        break
