import turtle

# 设置画笔的起始位置和方向
turtle.penup()
turtle.goto(-200, 100)
turtle.pendown()
turtle.setheading(0)

# 设置颜色模式为255
turtle.colormode(255)

# 设置画笔的线条宽度
turtle.pensize(1)

# 定义旗帜颜色
light_blue = (135, 206, 250)
pink = (255, 192, 203)
white = (255, 255, 255)

# 绘制五条长条
for i in range(5):
    turtle.penup()
    turtle.goto(-200, 80 - 40 * i + 5)
    turtle.pendown()
    if i == 0 or i == 4:
        turtle.fillcolor(light_blue)
        turtle.pencolor(light_blue)
    elif i == 2:
        turtle.fillcolor(white)
        turtle.pencolor(white)
    else:
        turtle.fillcolor(pink)
        turtle.pencolor(pink)
    turtle.begin_fill()
    for j in range(2):
        turtle.forward(400)
        turtle.right(90)
        turtle.forward(40)
        turtle.right(90)
    turtle.end_fill()
# 使用黑笔描边旗帜
turtle.penup()
turtle.goto(-200, 85)
turtle.pendown()
turtle.pencolor('black')
for i in range(2):
    turtle.forward(400)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)



# 隐藏画笔
turtle.hideturtle()

# 显示绘制结果
turtle.done()

