import turtle
import random

turtle.register_shape("images/pink_alien.gif")
turtle.register_shape("images/green_alien.gif")
turtle.register_shape("images/yellow_alien.gif")
turtle.register_shape("images/shooter.gif")
turtle.register_shape("images/bullet.gif")
turtle.register_shape("images/smoke.gif")


class Player(turtle.Turtle):
    # Main Character
    def __init__(self):
        super().__init__()
        self.shape("images/shooter.gif")
        self.color("#fffe35")
        self.penup()
        self.set_up()


    def set_up(self):
        self.settiltangle(40)
        self.goto(0, -250)


class Spaceship(turtle.Turtle):
    # Enemy Ship
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("red")
        self.shape(random.choice(["images/green_alien.gif", "images/yellow_alien.gif", "images/pink_alien.gif"]))

    def move_left(self):
        self.goto(self.xcor() + 100, self.ycor())


class Bullet(turtle.Turtle):
    def __init__(self, x, y, angle):
        super().__init__()
        self.shape("images/bullet.gif")
        self.penup()
        self.goto(x, y)
        self.setheading(angle)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 10)


class Star(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")


class Boss(turtle.Turtle):
    def __init__(self):
        super().__init__()


class Smoke(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("images/smoke.gif")


class Star(turtle.Turtle):
    def __init__(self, n):
        super().__init__()
        self.dist = n
        self.shape("circle")
        self.shapesize(n/10, n/10)
        self.color(random.choice(["#776f90", "#466962", "#5ca372"]))
        self.penup()
        self.goto(random.randint(-500, 500), 400 + random.randint(-300, 400))

    def fall(self):
        if self.ycor() < -350:
            self.goto(self.xcor() + random.randint(-10, 10), 400)
        else:
            self.goto(self.xcor() , self.ycor() - self.dist - random.randint(0, 2))