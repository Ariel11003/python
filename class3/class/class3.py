'''
name = 'Python'
age = 31
new_str = "我是" + name + "," + "今年" + str(age) + "歲了"
new_str_1 = "我是%s,今年%d歲了" % (name, age)
new_str_2 = "我是{},今年{}歲了".format(name, age)
new_str_3 = "我是{a},今年{b}歲了".(的)format(格式)(b=age, a=name)
重要⭐new_str_4 = f"我是{name},今年{age}歲了"

⭐try:
    num = int(input('請輸入一個數字'))
    total = num + 1
    print(total)
⭐except ValueError:
    print('請輸入數字')
可有可不有except:
    print('發生錯誤')
可有可不有else:
    print('成功執行')
可有可不有finally:
    print('程式結束')

    
'''

# try:
#     h = float(input('請輸入身高:'))
#     w = float(input('請輸入體重:'))
# except:
#     print('發生錯誤')
# else:
#     bmi = w / h**2
#     print('你的BMI為', bmi)
from operator import truediv


print(1==1)