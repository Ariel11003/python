# while True :
#     print("1. 蘋果汁")
#     print("2. 柳橙汁")
#     print("3. 葡萄汁")
#     print("4. 系統關閉")
#     nu=input("請輸入編號:")
#     if nu == "1":
#         print("您點蘋果汁")
#     elif nu =="2":
#         print("您點柳橙汁")
#     elif nu =="3":
#         print("您點葡萄汁")
#     elif nu == "4":
#         break
#     else:
#         print("請重新輸入")
import random
# print(random.randrange(3))
# print(random.randrange(0,10,2))
# print(random.randint(1,3))
# print(random.randint(1,10))

vvvvv=random.randint(1,100)
while True:
    ppt=int(input("輸入1~100:"))
    if vvvvv<ppt:
        print("再小一點")
    elif vvvvv>ppt:
        print("再大一點")
    else:
        print('恭喜')
        break
    