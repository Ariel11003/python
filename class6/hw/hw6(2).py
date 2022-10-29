"""
請輸入要印出的箭頭大小
​
hint:
可利用字串乘法
val="*" * 3
print(val)
***
​
EX:
請輸入要印出的箭頭大小:3
  *  
 *** 
*****
  *  
  *  
  * 
"""
x=int(input(''))
for i in range(x):
    print(" "*(x-i-1)+"*"*(i*2+1))
for p in range(x):
    print(" "*(x-1)+"*")
# print(' '*2+'*' *1)
# print(' '*1+'*' *3)
# print(' '*0+'*' *5)
# print(' '*2+'*' *1)
# print(' '*2+'*' *1)
# print(' '*2+'*' *1)