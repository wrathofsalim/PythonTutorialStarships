import pygame
import os

# https://www.youtube.com/watch?v=jO6qQDNa2UY : TUTORIAL 47.41


# region Options
WIDTH, HEIGHT = 1080, 740
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 45, 30
VELOCITY = 3
# endregion

# region Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

LIGHTRED = (255, 100, 100)
LIGHTGREEN = (100, 255, 0)
LIGHTBLUE = (100, 175, 255)

BROWN = (75, 50, 25)
PURPLE = (150, 0, 255)
PINK = (200, 100, 150)
ORANAGE = (200, 150, 100)
YELLOW = (200, 200, 100)
# endregion

# region Assets
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", "spaceship_yellow.png")
)
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),
    90,
)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),
    270,
)

SPACE_BACKGROUND_IMAGE = pygame.image.load(os.path.join("Assets", "space.png"))

BORDER = pygame.Rect((WIDTH / 2) - 5, 0, 10, HEIGHT)
# endregion


def draw_window(red, yellow):
    WIN.blit(SPACE_BACKGROUND_IMAGE, (0, 0), None, 0)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VELOCITY > 0:  # LEFT
        yellow.x -= VELOCITY
    if (
        keys_pressed[pygame.K_d]
        and yellow.x + VELOCITY + SPACESHIP_WIDTH / 2 < BORDER.x
    ):  # RIGHT
        yellow.x += VELOCITY
    if keys_pressed[pygame.K_w] and yellow.y - VELOCITY > 0:  # UP
        yellow.y -= VELOCITY
    if (
        keys_pressed[pygame.K_s]
        and yellow.y + VELOCITY + SPACESHIP_HEIGHT + SPACESHIP_HEIGHT / 2 < HEIGHT
    ):  # DOWN
        yellow.y += VELOCITY


def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VELOCITY > BORDER.x:  # LEFT
        red.x -= VELOCITY
    if (
        keys_pressed[pygame.K_RIGHT]
        and red.x + VELOCITY + SPACESHIP_WIDTH / 2 + SPACESHIP_WIDTH / 8 < WIDTH
    ):  # RIGHT
        red.x += VELOCITY
    if keys_pressed[pygame.K_UP] and red.y - VELOCITY > 0:  # UP
        red.y -= VELOCITY
    if (
        keys_pressed[pygame.K_DOWN]
        and red.y + VELOCITY + SPACESHIP_HEIGHT + SPACESHIP_HEIGHT / 2 < HEIGHT
    ):  # DOWN
        red.y += VELOCITY


def main():
    red = pygame.Rect(
        WIDTH / 2 + (WIDTH / 4), HEIGHT / 2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT
    )

    yellow = pygame.Rect(WIDTH / 4, HEIGHT / 2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        draw_window(red, yellow)

    pygame.quit()


if __name__ == "__main__":
    main()
