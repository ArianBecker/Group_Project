from components import *
from levels import *
import turtle
import time

GAME_ON = True


def create_level(level):
    spaceships = []
    for i in range(0, 5):
        for j in range(0, 3):
            if levels[level][j][i] == 1:
                spaceship = Spaceship()
                spaceship.goto(i * 100 - 200, j * 100 + 100)
                spaceships.append(spaceship)
    return spaceships


def main():
    # ________________________ Screen Set Up ________________________#
    sc = turtle.Screen()
    sc.setup(1000, 800)
    sc.bgcolor("#292d3e")
    sc.tracer(0)

    player = Player()
    spaceships = create_level(1)
    bullet = Bullet()
    sc.update()
    time.sleep(5000)
    for s in spaceships:
        s.move_left()
    sc.mainloop()

    sc.update()



if __name__ == "__main__": main()
