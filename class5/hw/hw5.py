"""
請使用turtle模組、for、time模組來印出時鐘的秒針
基本功能參考影片t1_turtle_time.mp4
提示：
turtle.clear() # 清空畫面指令
​
import time  # 匯入time模組
time.sleep(1) # 延遲1秒
"""
import turtle
import time
turtle.speed(0)
for a in range(0,360,6):
    turtle.right(a)
    turtle.forward(50)
    time.sleep(1)
    turtle.home()
    turtle.clear()
turtle.done()

