import pygame as pg
import sys, random


pg.init()

def draw_floor():
    window.blit(floor_img, (floor_x_pos,600))
    window.blit(floor_img, (floor_x_pos + 576,600))

def create_pipe():
    pipe_pos = random.choice(pipe_height)
    new_pipe = pipe_choice.get_rect(midtop=(700, pipe_pos))
    return new_pipe
    
def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -=5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        window.blit(pipe_choice, pipe)

# game variables
gravity = 0.25
bird_movement = 0

# first and second steps
window = pg.display.set_mode((576, 700))
clock = pg.time.Clock()

# thirdly loading and resizing of imagies(sprites)
bg_image = pg.image.load('assets/background-day.png').convert()
BG_SCALE = (576, 700) #scale the background to screen size
bg_image = pg.transform.scale(bg_image, BG_SCALE)

# load floor img
floor_img = pg.image.load('assets/base.png')
FLOOR_SCALE = (576, 150)
floor_img = pg.transform.scale(floor_img, FLOOR_SCALE)
floor_x_pos = 0

# bird image 
bird_img = pg.image.load("assets/bluebird-midflap.png")
# resize the bird image
bird_img = pg.transform.scale2x(bird_img)
bird_rect = bird_img.get_rect(center=(100, 350))
# next step is to make the bird fall by creating gravity 

# pipes imgs
red_pipe_img = pg.image.load("assets/pipe-red.png")
green_pipe_img = pg.image.load("assets/pipe-green.png")
pipe_list = [red_pipe_img, green_pipe_img]
pipe_choice = random.choice(pipe_list)
PIPE_SCALE = (52, 400)
pipe_choice = pg.transform.scale(pipe_choice, PIPE_SCALE)
# create a pipe_rect_list that is empty at first
pipe_rect_list = []
pipe_height = [400, 600, 800]
# create a timer that triggers the drawing of the pipes on screen
SPAWNPIPES = pg.USEREVENT
pg.time.set_timer(SPAWNPIPES, 1200)







while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                # print("flapp")
                bird_movement = 0
                bird_movement -=12
        if event.type == SPAWNPIPES:
            # print("pipe")
            pipe_rect_list.append(create_pipe())
            # print(pipe_rect_list)
            # create a function that move the pipes 

    window.blit(bg_image, (0,0))
    floor_x_pos -= 1
    draw_floor()
    # window.blit(floor_img, (floor_x_pos,550))
    if floor_x_pos <= -576:
        floor_x_pos = 0
    
    bird_movement += gravity
    bird_rect.centery += bird_movement
    window.blit(bird_img, bird_rect)

    pipe_rect_list = move_pipes(pipe_rect_list)
    draw_pipes(pipe_rect_list)
    



    clock.tick(120)




    pg.display.update()