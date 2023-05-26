import pygame
import random


class Paddle(pygame.Rect):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50.0
        self.height = 100.0

        self.speed = 5.0

    def Move(self, yDir):
        self.y += yDir * self.speed


class Ball(pygame.Rect):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.width = radius * 2
        self.height = radius * 2

        self.speed = 3.5
        self.direction = pygame.Vector2(-1, 0)

    def Move(self):
        self.x += self.direction.x * self.speed
        self.y += self.direction.y

    def OnPaddleHit(self, yDir):
        self.direction.y = yDir
        self.speed *= 1.05
        print(self.speed)

    def Reset(self, screen, scores, pointWinner):
        self.x = screen.get_width() / 2 - self.width / 2
        self.y = screen.get_height() / 2 - self.height / 2
        self.direction = pygame.Vector2(-1, 0)
        self.speed = 3.5
        scores[pointWinner] += 1
        print(f"{scores[0]} - {scores[1]}")


def Update():
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    clock = pygame.time.Clock()
    running = True

    paddle0 = Paddle(5, screen.get_height() / 2 - 50)
    paddle1 = Paddle(screen.get_width() - 55, screen.get_height() / 2 - 50)
    paddles = [paddle0, paddle1]
    scores = [0, 0]

    ball = Ball(screen.get_width() / 2.0 - 5.0, screen.get_height() / 2.0 - 5.0, 5.0)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        # Game loop starts here
        pygame.draw.rect(screen, (255, 0, 0), paddle0)
        pygame.draw.rect(screen, (0, 0, 255), paddle1)
        pygame.draw.rect(screen, (30, 30, 30), ball)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

        if keys[pygame.K_w]:
            paddle0.Move(-1)
            if paddle0.y < 0:
                paddle0.y = 0
        if keys[pygame.K_s]:
            paddle0.Move(1)
            if paddle0.bottom >= screen.get_height():
                paddle0.bottom = screen.get_height()
        if keys[pygame.K_UP]:
            paddle1.Move(-1)
            if paddle1.y < 0:
                paddle1.y = 0

        if keys[pygame.K_DOWN]:
            paddle1.Move(1)
            if paddle1.bottom > screen.get_height():
                paddle1.bottom = screen.get_height()

        if ball.y <= 0 or ball.bottom >= screen.get_height():
            ball.direction.y *= -1

        if ball.x <= 0:
            ball.Reset(screen, scores, 1)
        elif ball.x >= screen.get_width():
            ball.Reset(screen, scores, 0)

        collisions = ball.collidelistall(paddles)

        if len(collisions) > 0:
            ball.direction.x *= -1
            if collisions[0] == 0:
                yDir = (paddle0.centery - ball.centery) / 40.0
                ball.OnPaddleHit(yDir)
            if collisions[0] == 1:
                yDir = (paddle1.centery - ball.centery) / 40.0
                ball.OnPaddleHit(yDir)

        ball.Move()

        # Game loop ends here

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    Update()