'''
1.	請問Python有哪五種形態:
答案:int,float,str,bool,print
2.	請問使用什麼function可以顯示出形態
答案:重複
3.	請問 a = int('1'), a的形態是什麼
答案:
4.	請問 b = str(1), b的形態是什麼
答案:
5.	請問 c = float(1), c的形態是什麼
答案:
6.	請問 d = bool(1), d的形態是什麼
答案:
7.	請列出Python加、減、乘、除表示符號
答案:+,-,*,/
8. 請問今天學了哪一些function(函式)?
答案:
9. 延續上題, 請嘗試描述每個function的功能各別是什麼?
答案:
​
'''
"""
請使用者輸入身高(公尺)h以及體重(公斤)w
透過下面公式計算出BMI數值並顯示計算結果
​
bmi = w/h**2
​
EX:
請輸入身高:1.7
請輸入體重:50
你的BMI為17.301038062283737
"""
w=(input('請輸入身高'))
h=(input('請輸入體重'))
bmi =w/h**2
str(bmi)
print('你的BMI'+str(bmi ))
'''
old =input('請輸入歲數')
print("我是" + old +"歲")
'''