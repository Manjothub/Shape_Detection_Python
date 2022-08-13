import turtle as t

def square():
    t.TurtleScreen._RUNNING=True
    tw = t.Screen()
    for i in range(4):
        t.forward(100)
        t.right(90)
    tw.exitonclick()

def triangle():
    t.TurtleScreen._RUNNING=True
    tw = t.Screen()
    for i in range(3):
        t.forward(100)
        t.right(120)
    tw.exitonclick()

def star():
    t.TurtleScreen._RUNNING=True
    tw = t.Screen()
    for i in range(5):
        t.forward(150)
        t.right(144)
    tw.exitonclick()


square()
triangle()
star()