'''1+2+3.....
X=int(input("請輸入整數:"))
kk =0
for ooo in range(X+1):
    kk= kk+ooo
print(f'{X}{kk}')
'''
'''九九乘法程式
for p in range(1,10):
    for i in range(1,10):
        print(f'{p}X{i}={p*i}')
'''
'''質因數判別
x = int(input("請輸入正整數:"))
if x == 1:
    print(f"{x}不是質數")
else:
    i = 2
    while x % i != 0 and i != x:
        i += 1

    if i == x:
        print("yes")
    else:
        print("no")
'''

# i=0
# while i<5:
    #print(i) 
    # i +=1