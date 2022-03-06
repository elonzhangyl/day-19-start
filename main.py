import turtle

tim = turtle.Turtle()
s = 100
turtle.listen()


def fun_forwar():
    tim.forward(10)


def fun_backward():
    tim.backward(10)


def fun_clockwise():
    tim.right(5)


def fun_anticlockwise():
    tim.left(5)


def fun_clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


turtle.onkey(fun=fun_forwar, key="w")
turtle.onkey(fun=fun_backward, key="s")
turtle.onkey(fun=fun_clockwise, key="d")
turtle.onkey(fun=fun_anticlockwise, key="a")
turtle.onkey(fun=fun_clear, key="c")


turtle.listen()


turtle.mainloop()