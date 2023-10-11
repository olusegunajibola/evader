import pygame

WHITE = (255, 255, 255)

# initialize the game
pygame.init()

# create the screen            (width, height)
screen = pygame.display.set_mode((800, 600))

# title & icon
pygame.display.set_caption("Evader")
icon = pygame.image.load("space-ship.png")
pygame.display.set_icon(icon)

# Agent
agent = icon
agentX = 370  # X & Y are coordinates, i.e. positions
agentY = 480


def agent_draw():
    screen.blit(agent, (agentX, agentY))  # means to draw


# game loop
running = True
while running:

    screen.fill(WHITE)  # this will not work, an update display is needed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    agent_draw()
    pygame.display.update()
