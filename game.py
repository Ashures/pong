import pygame


class Paddle(pygame.Rect):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.speed = 5

    def Move(self, yDir):
        self.y += yDir * self.speed


def Update():
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        # Game loop starts here


        # Game loop ends here

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()