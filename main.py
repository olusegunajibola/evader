# import math
# import pygame
# import random
#
#
# WHITE = (255, 255, 255)
# number_of_obstacles = 4
# # initialize the game
# pygame.init()
#
# #                              (X    ,     Y)
# # create the screen            (width, height)
# screen = pygame.display.set_mode((800, 600))
#
# # background
# background = pygame.image.load("background.png")
#
# # title & icon
# pygame.display.set_caption("Evader")
# icon = pygame.image.load("space-ship.png")
# pygame.display.set_icon(icon)
#
# # obstacle
# obstacle = pygame.image.load("barrier.png")  # 124px
# obstacleX = random.randint(0, 700)
# obstacleY = random.randint(0, 550)
#
# print('obstacleX: ', obstacleX, 'obstacleY: ', obstacleY)
#
# agentX_change = 4  # 0.3
# agentY_change = 4  # 0.3
#
# # Agent
# agent = icon
# # agentX = 370  # X & Y are coordinates, i.e. positions
# # agentY = 480
#
# agentX = random.randint(1, 800)
# agentY = random.randint(1, 600)
#
#
# def agent_draw(x, y):
#     # screen.blit(agent, (agentX, agentY))  # means to draw
#     screen.blit(agent, (x, y))  # means to draw
#
#
# def obs_draw(x, y):
#     screen.blit(obstacle, (x, y))  # means to draw
#     # for i in range(1, number_of_obstacles):
#     #     screen.blit(obstacle, (x, y))  # means to draw
#
#
# def is_collision(obstacleX, obstacleY, agentX, agentY):
#     distance = math.sqrt((math.pow(agentX - obstacleX, 2))
#                          + (math.pow(agentY - obstacleY, 2)))
#
#     if distance < 45:
#         print(distance)
#         return True
#     else:
#         return False
#
#
# # game loop
# running = True
# while running:
#
#     # screen.fill(WHITE)  # this will not work, an update display is needed
#     screen.blit(background, (0, 0))
#
#     # agentY -= 0.1
#     agentY += agentY_change
#     agentX += agentX_change
#
#     # collision = is_collision(obstacleX, obstacleY, agentX, agentY)
#     # if collision:
#     #     print('before: ', agentX, agentY)
#     #     agentY -= agentY_change*2
#     #     # agentX += agentX_change
#     #     print('after: ', agentX, agentY)
#
#     # agentX -= 0.1
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     # contain within boundary of the game
#     if agentX <= 0:
#         # agentX = 0.5
#         agentX_change = 4
#     elif agentX >= 768:  # 768 is based on the value of the
#         # agent's pixel i.e 32px
#         # agentX = 767.5
#         agentX_change = -4
#
#     # contain within boundary of the game
#     if agentY <= 0:
#         agentY_change = 4
#     elif agentY >= 568:  # 568 is based on the value of the
#         # agent's pixel i.e 32px
#         # agentY = 567.5
#         agentY_change = -4
#
#     # print('agentX: ', agentX, 'agentY: ', agentY)
#
#     #  collision
#     # collision = is_collision(obstacleX, obstacleY, agentX, agentY)
#     # if collision:
#     #     agentY += 0.5
#
#     # # this works when the collision hits the top, but not bottom
#     # collision = is_collision(obstacleX, obstacleY, agentX, agentY)
#     # if collision:
#     #     print('before: ', agentX, agentY)
#     #     agentY_change = -4
#     #     # agentY -= agentY_change*2
#     #     # agentX += agentX_change
#     #     print('after: ', agentX, agentY)
#     #     print()
#
#     collision = is_collision(obstacleX, obstacleY, agentX, agentY)
#     if collision:
#         print('before: agent', agentX, agentY)
#         print('before: agent_change', agentX_change, agentY_change)
#         # agentY_change = -4
#         # agentX_change = -4
#
#         # this conditional statement checks it the agent is hitting the obstacle
#         # from below, if it does, it sends it backwards, otherwise, upwards.
#
#         if (agentX_change != -4) and (agentY_change != -4):
#             agentX_change = -random.randint(1, 10)
#             agentY_change = -random.randint(1, 10)
#         else:
#             agentX_change = random.randint(1, 10)
#             agentY_change = random.randint(1, 10)
#         print('after: ', agentX, agentY)
#         print('after: agent_change', agentX_change, agentY_change)
#         print()
#
#     # for i in range(1, number_of_obstacles):
#     #     obs_draw(obstacleX, obstacleY)
#     obs_draw(obstacleX, obstacleY)
#     # obs_draw(obstacleX, obstacleY)
#
#     agent_draw(agentX, agentY)  # enables the agent to move
#     # for i in range(1, number_of_obstacles):
#     #     obs_draw(obstacleX, obstacleY)
#     pygame.display.update()
#
# # TODO 0. insert 3 obstacles.
# # TODO 1. yet to fix the collision of 3 obstacles and evader agent
# # TODO 2. i think preference to go up has been fixed
# # TODO 3. If it hits the boundary, it should bounce back choosing any random direction
