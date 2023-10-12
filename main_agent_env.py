import pygame
import random
from Agent import Agent
from Environment import Environment
from obstacles import is_collision

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    env = Environment(500, 500)
    agent = Agent(250, 250)

    number_of_obstacles = 4

    agentX_change = 4  # default movement parameters
    agentY_change = 4

    # game loop
    running = True
    while running:
        screen.blit(env, (0, 0))

        agent.y += agentY_change
        agent.x += agentX_change

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for i in range(number_of_obstacles):
            # contain agent within horizontal (X) boundary of the game
            if agent.x <= 0:
                agentX_change = 4
            elif agent.x >= 768:  # 768 is based on the value of the
                # agent's pixel i.e 32px
                agentX_change = -4

            # contain agent within vertical (Y)  boundary of the game
            if agent.y <= 0:
                agentY_change = 4
            elif agent.y >= 568:  # 568 is based on the value of the
                # agent's pixel i.e 32px
                agentY_change = -4

            collision = is_collision(Environment.obst_loop(number_of_obstacles)[1][i],
                                     Environment.obst_loop(number_of_obstacles)[2][i],
                                     agent.x, agent.y)
            if collision:
                if (agentX_change != -4) and (agentY_change != -4):
                    agentX_change = -random.randint(1, 10)
                    agentY_change = -random.randint(1, 10)
                else:
                    agentX_change = random.randint(1, 10)
                    agentY_change = random.randint(1, 10)

        # env.obs_draw(, screen)
        agent.agent_draw(screen)
        pygame.display.update()

    pygame.quit()
