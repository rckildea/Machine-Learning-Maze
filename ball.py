import pygame


class Ball:
    def __init__(self):
        BLACK = (0, 0, 0)
        self.ball_image = pygame.image.load("media/ball.png").convert_alpha()
        self.ball_image.set_colorkey(BLACK)
        self.ball_pos_x = 10
        self.ball_pos_y = 10
        self.ball_vel_x = 0
        self.ball_vel_y = 0
        self.ball_rect = self.ball_image.get_rect()
        self.update_rect()
        self.ball_mask = pygame.mask.from_surface(self.ball_image)

    def update_rect(self):
        self.ball_rect.x = self.ball_pos_x
        self.ball_rect.y = self.ball_pos_y

    def draw(self, display):
        display.blit(self.ball_image, (self.ball_pos_x, self.ball_pos_y))
        self.update_rect()

    def handle_input(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.ball_vel_x -= 2
        elif keys[pygame.K_RIGHT]:
            self.ball_vel_x += 2

        if keys[pygame.K_UP]:
            self.ball_vel_y -= 2
        elif keys[pygame.K_DOWN]:
            self.ball_vel_y += 2

    def step(self, maze):
        self.ball_pos_x += self.ball_vel_x
        self.ball_pos_y += self.ball_vel_y

        self.ball_vel_x = 0
        self.ball_vel_y = 0
        self.update_rect()

        if self.check_crash(maze):
            print("Crash!")
            self.ball_pos_x = 10
            self.ball_pos_y = 10

    def check_crash(self, maze):
        if self.ball_pos_x < 0 or self.ball_pos_x > 600 or self.ball_pos_y < 0 or self.ball_pos_y > 600:
            return True
        offset_x, offset_y = (maze.maze_rect.left - self.ball_rect.left), (maze.maze_rect.top - self.ball_rect.top)
        if self.ball_mask.overlap(maze.maze_mask, (offset_x, offset_y)) is not None:
            return True
        if self.ball_rect.colliderect(maze.platform_rect):
            print("WINNER!")