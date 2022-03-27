import turtle

admiral = turtle.Turtle()
admiral.speed(10)


def set_position(pos_x, pos_y):
    admiral.setx(pos_x)
    admiral.sety(pos_y)


def draw_square(size):
    for i in range(4):
        admiral.forward(size)
        admiral.right(90)


def draw_triangle(size):
    for i in range(3):
        admiral.forward(size)
        admiral.left(120)


# Square Section
def square_section():
    admiral.fillcolor("#003049")

    admiral.penup()
    set_position(-300, 250)
    admiral.pendown()

    admiral.begin_fill()
    draw_square(120)
    admiral.end_fill()

    admiral.penup()
    set_position(-130, 240)
    admiral.pendown()

    admiral.begin_fill()
    draw_square(42)
    admiral.end_fill()

    admiral.penup()
    set_position(-140, 160)
    admiral.pendown()

    admiral.begin_fill()
    draw_square(37)
    admiral.end_fill()

    admiral.penup()
    set_position(-200, 100)
    admiral.pendown()

    admiral.begin_fill()
    draw_square(32)
    admiral.end_fill()

    admiral.penup()
    set_position(-290, 90)
    admiral.pendown()

    admiral.begin_fill()
    draw_square(47)
    admiral.end_fill()


# Circle Section
def circle_section():
    admiral.fillcolor("#06D6A0")

    admiral.penup()
    set_position(230, 250)
    admiral.pendown()

    admiral.begin_fill()
    admiral.circle(-70)
    admiral.end_fill()

    admiral.penup()
    set_position(125, 260)
    admiral.pendown()

    admiral.begin_fill()
    admiral.circle(-20)
    admiral.end_fill()

    admiral.penup()
    set_position(105, 180)
    admiral.pendown()

    admiral.begin_fill()
    admiral.circle(-30)
    admiral.end_fill()

    admiral.penup()
    set_position(170, 95)
    admiral.pendown()

    admiral.begin_fill()
    admiral.circle(-15)
    admiral.end_fill()

    admiral.penup()
    set_position(260, 80)
    admiral.pendown()

    admiral.begin_fill()
    admiral.circle(-25)
    admiral.end_fill()


# Triangle Section
def triangle_section():
    admiral.fillcolor("#D62828")

    admiral.penup()
    set_position(-300, -220)
    admiral.pendown()

    admiral.begin_fill()
    draw_triangle(120)
    admiral.end_fill()

    admiral.penup()
    set_position(-295, -90)
    admiral.pendown()

    admiral.begin_fill()
    draw_triangle(50)
    admiral.end_fill()

    admiral.penup()
    set_position(-190, -130)
    admiral.pendown()

    admiral.begin_fill()
    draw_triangle(70)
    admiral.end_fill()

    admiral.penup()
    set_position(-130, -190)
    admiral.pendown()

    admiral.begin_fill()
    draw_triangle(30)
    admiral.end_fill()

    admiral.penup()
    set_position(-160, -250)
    admiral.pendown()

    admiral.begin_fill()
    draw_triangle(40)
    admiral.end_fill()


# Drawing the Square Section
square_section()

# Drawing the Circle Section
circle_section()

# Drawing the Triangle Section
triangle_section()

turtle.done()
