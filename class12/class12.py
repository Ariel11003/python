# # 以整數表示
# print('I %d savage' % 94)
# # 以 3 個字元寬度顯示整數，不滿 3 個則補空白
# print('I %3d savage' % 94)
# # 以 3 個字元寬度顯示整數，不滿 3 個則補 0
# print('I %03d savage' % 94)


# # 以整數表示
# print("I {0:d} savage".format(94))
# # 以 3 個字元寬度顯示整數，不滿 3 個則補空白
# print("I {0:3d} savage".format(94))
# #以 3 個字元寬度顯示整數，不滿 3 個則補 0
# print("I {0:03d} savage".format(94))

# # 以浮點數表示，預設小數位數為 6 位
# print('I %f savage' %94)
# # 以浮點數表示，設定小數位數為 2 位
# print('I %.2f savage' %94)

# # 以浮點數表示，預設小數位數為 6 位
# print('I {0:f} savage'.format(94))
# # 以浮點數表示，設定小數位數為 2 位
# print('I {0:.2f} savage'.format(94))

# # 以字串表示
# print('I %s savage' %'94')
# # 以字串表示
# print('I {0:s} savage'.format('94'))

# # 可以自動辨識傳入的字串是不是運算式
# ans = eval("1+2")
# print(ans)
# ans = eval("a+b")
# print(ans)


# import datetime
# print(datetime.date.today())

# import datetime
# Date = datetime.date.today()
# print(Date) #年月日
# print(Date.year) #年 
# print(Date.month) #月
# print(Date.day) #日

# import datetime
# #datetime to string
# Date = datetime.date.today()
# print(Date.strftime('%d %b %B %Y %y %A %a'))

import datetime
day = input("What is your birthday? ")
print(day)
birth = datetime.datetime.strptime(day, "%Y/%m/%d")
print(birth.date())
