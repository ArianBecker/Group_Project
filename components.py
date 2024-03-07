import turtle


turtle.register_shape("images/alien.gif")
turtle.register_shape("images/shooter.gif")
turtle.register_shape("images/bullet.gif")


class Player(turtle.Turtle):
    # Main Character
    def __init__(self):
        super().__init__()
        self.shape("images/shooter.gif")
        self.color("#fffe35")
        self.penup()
        self.set_up()

    def set_up(self):
        self.goto(0, -250)


class Spaceship(turtle.Turtle):
    # Enemy Ship
    def __init__(self):
        super().__init__()
        self.shape("images/alien.gif")
        self.penup()
        self.color("red")

    def move_left(self):
        self.goto(self.xcor() + 100, self.ycor())


class Bullet(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("images/bullet.gif")


class Star(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")