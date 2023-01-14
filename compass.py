import turtle
from time import sleep

t = turtle.Turtle()


def setupStuff():
    turtle.screensize(5000, 5000)
    t.hideturtle()
    t.penup()
    t.speed(0)
    # turtle.tracer(0, 0)


def get_mouse_click_coor(x, y):
    print(int(x), int(y))


def get_coor():
    turtle.onscreenclick(get_mouse_click_coor)
    turtle.mainloop()


def thinPen():
    t.color("grey")
    t.pensize(1)


def thiccPen():
    t.color("black")
    t.pensize(3)


def drawThinCircle(x, y, radius):
    t.goto(x, y - radius)
    thinPen()

    t.pendown()
    t.circle(radius)
    t.penup()


def drawThiccCircle(x, y, radius, startingBearing, endingBearing):
    drawThinCircle(x, y, radius)
    thiccPen()
    t.circle(radius, 180 - endingBearing)

    t.pendown()
    t.circle(radius, endingBearing - startingBearing)
    t.penup()

    t.circle(radius, startingBearing + 180)


def drawThinLine(x1, y1, x2, y2):
    thinPen()
    t.goto(x1, y1)

    t.pendown()
    t.goto(x2, y2)
    t.penup()


def drawThiccLine(x1, y1, x2, y2):
    thiccPen()
    t.goto(x1, y1)

    t.pendown()
    t.goto(x2, y2)
    t.penup()


def runScript(listOfLines):
    for line in listOfLines:
        parameterList = line.split(' ')

        # circle
        if len(parameterList) == 3:
            drawThinCircle(
                int(parameterList[0]) // 4,
                int(parameterList[1]) // 4,
                int(parameterList[2]) // 4
            )

        # line
        elif len(parameterList) == 4:
            drawThinLine(
                int(parameterList[0]) // 4,
                int(parameterList[1]) // 4,
                int(parameterList[2]) // 4,
                int(parameterList[3]) // 4
            )

        # strong line
        elif parameterList[0] == "strong":
            drawThiccLine(
                int(parameterList[1]) // 4,
                int(parameterList[2]) // 4,
                int(parameterList[3]) // 4,
                int(parameterList[4]) // 4
            )

        # arc
        else:
            drawThiccCircle(
                int(parameterList[0]) // 4,
                int(parameterList[1]) // 4,
                int(parameterList[2]) // 4,
                int(parameterList[3]),
                int(parameterList[4])
            )


def main():
    setupStuff()
    sleep(5)
    runScript(open("script.txt", 'r').readlines())
    turtle.update()
    turtle.Screen().getcanvas().postscript(file='outputname.ps', pagewidth=10000, pageheight=10000, height=10000, width=10000)
    get_coor()


if __name__ == '__main__':
    main()
