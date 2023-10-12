import math
import pygame
import random

# WHITE = (255, 255, 255)
number_of_obstacles = 4

# initialize the game
pygame.init()

#                              (X    ,     Y)
# create the screen            (width, height)
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load("background.png")

# title & icon
pygame.display.set_caption("Space Evader")
icon = pygame.image.load("space-ship.png")
pygame.display.set_icon(icon)

# obstacles
obstacle = []
obstacleX = []
obstacleY = []

for i in range(number_of_obstacles):
    obstacle.append(pygame.image.load("barrier.png"))  # 124px
    obstacleX.append(random.randint(50, 700))
    obstacleY.append(random.randint(50, 550))

agentX_change = 4  # default movement parameters
agentY_change = 4

# Agent
agent = icon
# X & Y are coordinates, i.e. positions, they are random for the agent
agentX = random.randint(1, 800)
agentY = random.randint(1, 600)


def agent_draw(x, y):
    screen.blit(agent, (x, y))  # means to draw


def obs_draw(x, y, ind):
    screen.blit(obstacle[ind], (x, y))  # means to draw


def is_collision(obstaclex, obstacley, agentx, agenty):
    distance = math.sqrt((math.pow(agentx - obstaclex, 2))
                         + (math.pow(agenty - obstacley, 2)))
    if distance < 45:
        # print(distance)
        return True
    else:
        return False


# game loop
running = True
while running:

    # screen.fill(WHITE)  # this will not work, an update display is needed
    screen.blit(background, (0, 0))

    agentY += agentY_change
    agentX += agentX_change

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(number_of_obstacles):
        # contain agent within horizontal (X) boundary of the game
        if agentX <= 0:
            agentX_change = 4
        elif agentX >= 768:  # 768 is based on the value of the
            # agent's pixel i.e 32px
            agentX_change = -4

        # contain agent within vertical (Y)  boundary of the game
        if agentY <= 0:
            agentY_change = 4
        elif agentY >= 568:  # 568 is based on the value of the
            # agent's pixel i.e 32px
            agentY_change = -4

        collision = is_collision(obstacleX[i], obstacleY[i], agentX, agentY)
        if collision:
            # print('before: agent', agentX, agentY)
            # print('before: agent_change', agentX_change, agentY_change)

            # this conditional statement checks it the agent is hitting the obstacle
            # from below, if it does, it sends it backwards, otherwise, upwards.
            if (agentX_change != -4) and (agentY_change != -4):
                agentX_change = -random.randint(1, 10)
                agentY_change = -random.randint(1, 10)
            else:
                agentX_change = random.randint(1, 10)
                agentY_change = random.randint(1, 10)
            # print('after: ', agentX, agentY)
            # print('after: agent_change', agentX_change, agentY_change)
            # print()

    for i in range(number_of_obstacles):
        obs_draw(obstacleX[i], obstacleY[i], i)

    agent_draw(agentX, agentY)  # enables the agent to move

    pygame.display.update()
