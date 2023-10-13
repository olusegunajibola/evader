import pygame
import random
import math

# title & icon
pygame.display.set_caption("Space Evader")
icon = pygame.image.load("space-ship.png")
pygame.display.set_icon(icon)

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
    def backg(backg_=background):
        return backg_

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
    def is_collision(obstaclex, obstacley, agentx, agenty, threshold=45):
        distance = math.sqrt((math.pow(agentx - obstaclex, 2))
                             + (math.pow(agenty - obstacley, 2)))
        if distance < threshold:
            # print(distance)
            return True
        else:
            return False

    @staticmethod
    def obs_draw(obs, obs_x, obs_y, screen):
        screen.blit(obs, (obs_x, obs_y))  # means to draw

    # @staticmethod
    # def obs_draw(self, x, y, ind, screen):
    #     screen.blit(self.obst_loop.obstacle[ind], (self.x, self.y))  # means to draw
