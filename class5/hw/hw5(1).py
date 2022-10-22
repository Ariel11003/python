"""
請使用turtle模組以及for印出以下圖形
t0_turtle_stamp.jpg
提示：
turtle.home()是讓烏龜回到原點的指令
"""
import turtle 
turtle.penup()
for a in range(0,360,45):
    turtle.right(a)
    turtle.forward(50)
    turtle.stamp()
    turtle.home()
turtle.done()



