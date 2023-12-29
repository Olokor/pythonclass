import pygame as pg
import sys
import random

pg.init()

# Set up the window
window_size = (576, 700)
window = pg.display.set_mode(window_size)

# Load the background image
SURFACE_IMAGE_SCALAR = (576, 700)
bg = pg.image.load('bgpic.jpeg').convert()
bg_surface = pg.transform.scale(bg, SURFACE_IMAGE_SCALAR)

# Load the sprites
apple = pg.image.load("apple.png").convert_alpha()
APPLE_SIZE = (100, 100)
apple = pg.transform.scale(apple, APPLE_SIZE)
BOWL_SIZE = (150, 150)
bowl = pg.image.load("test2.png")
bowl = pg.transform.scale(bowl, BOWL_SIZE)

# Initial positions
apple_pos = pg.Vector2(random.randint(0, window_size[0] - APPLE_SIZE[0]), 0)
bowl_pos = pg.Vector2(0, 600)

# Set up clock
clock = pg.time.Clock()

# Game variables
score = 0

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # Check if apple is at the top, then set a new random x-position
    if apple_pos.y >= window_size[1]:
        apple_pos.x = random.randint(0, window_size[0] - APPLE_SIZE[0])
        apple_pos.y = 0

    # Update apple position (falling down)
    apple_pos.y += 5  # Adjust the falling speed as needed

    # Update bowl position (moving left to right)
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        bowl_pos.x -= 5
    if keys[pg.K_RIGHT]:
        bowl_pos.x += 5

    # Create Rect objects for collision detection
    apple_rect = pg.Rect(apple_pos-(50,50), APPLE_SIZE)
    bowl_rect = pg.Rect(bowl_pos, BOWL_SIZE)

    # Collision detection
    if bowl_rect.colliderect(apple_rect):
        # Apple caught, increment score and reset apple position
        score += 1
        apple_pos.x = random.randint(0, window_size[0] - APPLE_SIZE[0])
        apple_pos.y = 0

    window.blit(bg_surface, (0, 0))
    window.blit(apple, apple_pos)
    window.blit(bowl, bowl_pos)

    # Display score
    font = pg.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    window.blit(score_text, (10, 10))

    pg.display.flip()

    clock.tick(60)  # Adjust the frame rate as needed
