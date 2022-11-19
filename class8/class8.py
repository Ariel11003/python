'''
import random as r

a = 100
b = 0
x = r.randrange(0, 101)
while True:
    ans = int(input(f"請輸入{b}~{a}的整數:"))
    if ans > x:
        print('在小一點')
        if b < ans < a:
            a = ans
    elif ans < x:
        print('在大一點')
        if b < ans < a:
            b = ans
    else:
        print('~恭喜猜中了!~')
        break
    ['蘋果', '香蕉', '葡萄']
'''
'''
[]
['蘋果']
['a', 'b']
[1, 2, 3]

[1, 2] + ['b', 'c']

[1, 2] * 2

l = ['a', 'b', 'c']
l[0]
l[1]
l[2]

l = [0, 1, 2, 3, 4]
l[0:3]
l[3:5]

len([])
len(['蘋果'])
len(['a', 'b'])
len([1, 2, 3])

l = ['a', 'b', 'c']
for index in range(len(l)):
    print(l[index])

l = ['a', 'b', 'c']
for element in l:
    print(element)

max([])
max(['蘋果', '香蕉', '橘子'])
max(['a', 'b'])
max([1, 2, 3])

min([])
min(['蘋果', '香蕉', '橘子'])
min(['a', 'b'])
min([1, 2, 3])

list('abc')
list([4, 5, 6])
list(range(3))
'1,2,3'.split(',')
'2020/1/1'.split('/')

img = ['1', '2', '3']
'-'.join(img)

l = ['a', 'b', 'c']
a = l.copy()
a[0] = 1
print(a, l)
'''
#l=['a','b','c']
#l
#l[0]='A'
#l

juice=['蘋果汁','柳橙汁','葡萄汁','原神','系統關閉']
while True:
    for i in range (len(juice)):
        print(f'{i+1}.{juice[i]}')

    ans = int(input("請輸入編號:"))
    if ans == len(juice):
        print("~~系統關閉~~")
        break
    elif ans > len(juice) or ans <= 0:
        print("輸入錯誤查無此果汁，請重新輸入")
    else:
        print(f"您點的商品是{juice[ans-1]}")
        

#    print("1. 蘋果汁")
#    print("2. 柳橙汁")
#    print("3. 葡萄汁")
#    print("4. 系統關閉")

