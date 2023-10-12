from Agent import Agent
import pygame
import random
import math

from obstacles import obstacle

# background
background = pygame.image.load("background.png")

# barrier
barrier = pygame.image.load("barrier.png")


class Environment:

    def __init__(self, width, height):
        assert isinstance(width, int) and isinstance(height, int)
        self._width = width
        self._height = height

    @staticmethod
    def obst_loop(number_of_obstacles):
        obstacle_list = []
        obstacle_x = []
        obstacle_y = []
        for i in range(number_of_obstacles):
            obstacle_list.append(barrier)  # 124px
            obstacle_x.append(random.randint(50, 700))
            obstacle_y.append(random.randint(50, 550))
        return obstacle_list, obstacle_x, obstacle_y

    @staticmethod
    def is_collision(obstaclex, obstacley, agentx, agenty):
        distance = math.sqrt((math.pow(agentx - obstaclex, 2))
                             + (math.pow(agenty - obstacley, 2)))
        if distance < 45:
            # print(distance)
            return True
        else:
            return False

    def obs_draw(self, x, y, ind, screen):
        screen.blit(self.obst_loop.obstacle[ind], (self.x, self.y))  # means to draw


