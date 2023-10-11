import pygame

WHITE = (255, 255, 255)

# initialize the game
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# title & icon
pygame.display.set_caption("Evader")
icon = pygame.image.load("space-ship.png")
pygame.display.set_icon(icon)


# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((WHITE)) # this will not work, an update display is needed
    pygame.display.update()