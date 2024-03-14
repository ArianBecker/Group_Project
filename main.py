from components import *
from levels import *
import turtle
import threading
import time

GAME_ON = True

def big_bag():
    stars = []
    for i in range(0, 30):
        stars.append(Star(random.randint(2,5)))
    return stars

def snow(stars):
    for star in stars:
        star.fall()



def create_level(level):
    spaceships = []
    for i in range(0, 5):
        for j in range(0, 3):
            if levels[level][j][i] == 1:
                spaceship = Spaceship()
                spaceship.goto(i * 100 - 200, j * 100 + 100)
                spaceships.append(spaceship)
    return spaceships


def clear_level(spaceships):
    for spaceship in spaceships:
        spaceship.hideturtle()


def main():
    # ________________________ Screen Set Up ________________________#
    sc = turtle.Screen()
    sc.setup(1000, 800)
    sc.bgcolor("#292d3e")
    sc.tracer(False)


    player = Player()
    player.tiltangle(30)
    print(player.heading())
    bullet = Bullet(player.xcor(), player.ycor(), player.heading())
    create_level(1)

    stars = big_bag()

    while GAME_ON:
        snow(stars)
        sc.update()
        bullet.up()
        time.sleep(0.02)

    sc.mainloop()


if __name__ == "__main__": main()
