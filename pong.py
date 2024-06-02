import pygame, sys, random

pygame.init()

WIDTH, HEIGHT = 900, 770

FONT = pygame.font.SysFont("Consolas", int(WIDTH / 20))

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong!")
CLOCK = pygame.time.Clock()


# Paddles

player = pygame.Rect(WIDTH - 50, HEIGHT / 2 - 50, 10, 100)
opponent = pygame.Rect(50, HEIGHT / 2 - 50, 10, 100)
player_score, opponent_score = 0, 0

paddle_speed = 3

# Ball

ball = pygame.Rect(WIDTH / 2 - 10, HEIGHT / 2 - 10, 20, 20)
x_speed, y_speed = 1, 1
speed = 1
speed_increment = 0.1

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_UP]:
        if player.top > 0:
            player.top -= paddle_speed
    elif keys_pressed[pygame.K_DOWN]:
        if player.bottom < HEIGHT:
            player.bottom += paddle_speed

    if ball.y > HEIGHT - 10:
        y_speed = -1
    if ball.y <= 0:
        y_speed = 1
    if ball.x <= 0:
        player_score += 1
        ball.center = (WIDTH / 2, HEIGHT / 2)
        x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])
        # speed = 1
    if ball.x >= WIDTH:
        opponent_score += 1
        ball.center = (WIDTH / 2, HEIGHT / 2)
        x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])
        # speed = 1

    if player.x - ball.width <= ball.x <= player.x and ball.y in range(
        player.top - ball.width, player.bottom - ball.width
    ):
        x_speed = -1
        speed += speed_increment

    if opponent.x - ball.width <= ball.x <= opponent.x and ball.y in range(
        opponent.top - ball.width, opponent.bottom - ball.width
    ):
        x_speed = 1
        speed += speed_increment

    ball.x += x_speed * speed
    ball.y += y_speed * speed

    if opponent.top < ball.y:
        opponent.top += paddle_speed + 5
        # if opponent.top > HEIGHT - opponent.height:
        #     opponent.top = HEIGHT - opponent.height

    if opponent.bottom > ball.y:
        opponent.bottom -= paddle_speed + 5
        # if opponent.bottom < 0:
        #     opponent.bottom = 0

    player_score_text = FONT.render(str(player_score), True, "white")
    opponent_score_text = FONT.render(str(opponent_score), True, "white")

    SCREEN.fill("black")

    pygame.draw.rect(SCREEN, "white", player)
    pygame.draw.rect(SCREEN, "white", opponent)
    pygame.draw.circle(SCREEN, "white", ball.center, 10)

    pygame.draw.line(SCREEN, "white", (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 1)

    SCREEN.blit(opponent_score_text, (WIDTH // 2 - 80, 50))
    SCREEN.blit(player_score_text, (WIDTH // 2 + 50, 50))

    pygame.display.update()
    CLOCK.tick(300)
