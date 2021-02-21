import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

snake_display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake Game by Wellington College')

game_over = False

snake_x = 300
snake_y = 300
snake_size = 10
snake_x_change = 0
snake_y_change = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -10
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = 10
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -10
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = 10
                snake_x_change = 0

    snake_x += snake_x_change
    snake_y += snake_y_change
    snake_display.fill(white)
    pygame.draw.rect(snake_display, black, [snake_x, snake_y, snake_size, snake_size])

    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()