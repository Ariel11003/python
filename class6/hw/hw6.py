"""
輸入一數字n為尋找的區間範圍, 找出區間範圍
3,7的倍數顯示在螢幕上, 其餘不顯示
​
hint:可以使用%取餘數進行判斷
​
EX
請輸入正整數:20
3
6
7
9
12
14
15
18
"""
i=int(input(''))
for p in range(1, i):
    if p%3==0:
        print(p)
    elif p%7==0:
        print(p)
