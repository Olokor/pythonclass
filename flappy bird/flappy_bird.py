import pygame as pg
import sys

pg.init()

# first and second steps
window = pg.display.set_mode((576, 700))
clock = pg.time.Clock()

# thirdly loading and resizing of imagies(sprites)
bg_image = pg.image.load('asse')


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    


    clock.tick(120)




    pg.display.update()