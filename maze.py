import pygame


class Maze:
    def __init__(self, maze_num):
        BLACK = (0, 0, 0)
        self.maze_number = maze_num
        self.maze_image = pygame.image.load("media/mazes/maze{}.png".format(self.maze_number)).convert()
        self.maze_image.set_colorkey(BLACK)
        self.platform_image = pygame.image.load("media/platform.png").convert_alpha()
        self.platform_coords = (120, 140)
        self.platform_rect = self.platform_image.get_rect()
        self.platform_rect.x, self.platform_rect.y = self.platform_coords

        self.maze_rect = self.maze_image.get_rect()
        self.maze_mask = pygame.mask.from_surface(self.maze_image)

    def draw(self, display):
        display.blit(self.maze_image, (0, 0))
        display.blit(self.platform_image, self.platform_coords)