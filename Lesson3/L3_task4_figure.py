from turtle import *
my_t = Turtle()
my_t.screen.setup(1200, 800)
my_t.screen.bgcolor("light blue")
my_t.speed(15)
my_t.ht()


# Рисуем тело
def sq_cr(side):
    my_t.width(8)
    my_t.color("yellow")
    my_t.circle(side / 3, 360)
    my_t.left(-220)
    my_t.circle(side / 2, 360)

    my_t.up()
    my_t.goto(-15, -20)
    my_t.down()
    my_t.circle(20, -180)

    my_t.up()
    my_t.goto(35,30)
    my_t.down()
    for i in range(2):
        my_t.width(3)
        my_t.color("orange red")
        my_t.fd(15)
        my_t.left(35)
        my_t.bk(15)
        my_t.right(15)


    my_t.up()
    my_t.goto(15,35)
    my_t.down()

    for eye in range(1):

        my_t.color("green")
        my_t.width(2)
        my_t.circle(7)
        my_t.width(4)
        my_t.circle(3)  

    my_t.up()
    my_t.goto(-45,-90)
    my_t.down()

    for paws in range(1):
        my_t.width(10)
        my_t.color("Red")
        my_t.left(-80)
        my_t.fd(15)

    my_t.up()
    my_t.goto(-40,-110)
    my_t.down()

    for hand in range(3):
        my_t.fd(10)
        my_t.left(120)    

    my_t.up()
    my_t.goto(-20,-90)
    my_t.down()

    for paws in range(1):
        my_t.width(10)
        my_t.color("Red")
        my_t.left(0)
        my_t.fd(15)


    my_t.up()
    my_t.goto(-17,-110)
    my_t.down()

    for hand in range(3):
        my_t.forward(10)
        my_t.left(120)

sq_cr(100)

my_t.screen.exitonclick()
my_t.screen.mainloop()