import random
import pygame

# Agent
agent = pygame.image.load("space-ship.png")


class Agent:

    def __init__(self, x, y):
        # assert

        agent_x = random.randint(1, 800)
        agent_y = random.randint(1, 600)

        self.x = agent_x
        self.y = agent_y

    def agent_draw(self, screen):
        screen.blit(agent, (self.x, self.y))  # draw agent
