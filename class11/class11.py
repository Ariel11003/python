# def hi (name):
#     print(f"hi{name}")

# hi(input("請輸入名子"))

# def eyyyy(a,b):
#     if a<b:
#         return a
#     else:
#         return b

# x= eyyyy (1,2)
# print("eyyyy:",x)
import random

def a(n):
    dice = []
    for i in range(n):
        dice.append(random.randint(1,6))
    return dice
cnt = int(input("輸入次數"))
print(a(cnt))

