import pygame
import ball
import maze

resolution = (600, 600)
display = pygame.display.set_mode(resolution)
pygame.display.set_caption("Machine Learning Maze")
clock = pygame.time.Clock()

ball = ball.Ball()
maze = maze.Maze(1)

def game_loop():

    while True:
        display.fill((0, 0, 0))
        maze.draw(display)
        ball.draw(display)
        ball.handle_input()
        ball.step(maze)



        pygame.display.update()

        clock.tick(60)


game_loop()