import pygame as py
from pygame import QUIT

py.init()

window_wight = 800
window_height = 750

playzone_width = ""
playzone_height = ""



display = py.display.set_mode((window_wight,    window_height))
py.display.set_caption("Bullet Hell !")



#Color

blue = (0, 0, 255)

display.fill(blue)

player_model = py.image.load("assert/2BlueWizardIdle/Chara - BlueIdle00000.png")
player_model = py.transform.scale(player_model, (100, 100))
clock = py.time.Clock()



class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.walkcount = 0

    def draw_player(self, display):
        if self.walkcount + 1 >= 27:
            self.walkcount = 0
        else:
            display.blit(player_model, (self.x, self.y))





def main_game():

    def redraw():
        display.fill(blue)
        man.draw_player(display)
        py.display.update()

    man = player(100, 410, 20, 20)
    run = True
    while run:
        clock.tick(60)
        for event in py.event.get():
            if event.type == QUIT:
                run = False
                py.quit()

        keys = py.key.get_pressed()
        if keys[py.K_LEFT] and man.x > man.velocity:
            man.x -= man.velocity
        elif keys[py.K_RIGHT] and man.x < 500 - man.width - man.velocity:
            man.x += man.velocity
        elif keys[py.K_UP] and man.y > man.velocity:
            man.y -= man.velocity
        elif keys[py.K_DOWN] and man.y < 650 - man.height - man.velocity:
            man.y += man.velocity

        redraw()
        py.display.update()

def main():
    main_game()


main()