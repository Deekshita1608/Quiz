def congrats():
    import turtle
    import random
    import time

    vij=turtle.Turtle()

    vij.getscreen().bgcolor("black")


    #congo
    vij.color("gold")
    style=('Great Vibes',50,'bold')
    vij.write("Congratulations!!",font=style,align='center')

    #FIREWORKS
    def firework(a):
        x=random.randint(-300,300)
        y=random.randint(-300,300)

        vij.speed(100)

        vij.penup()
        vij.goto(x,y)
        vij.pendown()

        s=random.randint(50,250)

        vij.color(a)
        for i in range (36):
            vij.forward(s)
            vij.backward(s)
            vij.left(10)

    li=['lime','orange','blueviolet','honeydew','violet','silver','gold','darkorange','deeppink','aquamarine','lightgreen']
    for x in range(0,6):
        color=random.choice(li)
        firework(color)
    time.sleep(2)
    turtle.bye()


