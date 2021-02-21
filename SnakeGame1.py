import pygame
import random

pygame.init()
white = (255, 255, 255)
colour =  (123, 32, 21)
black = (0,0,0)
snake_display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake Game by Wellington College KFW')
game_over = False
snake_x = 300
snake_y = 300
snake_size = 10
clear = False
num_food = 5
snake_distance = 10
snake_speed = 30
clock = pygame.time.Clock()
snake_x_change = 0
snake_y_change = 0
snake_food_x = []
snake_food_y = []


for i in range(num_food):
    snake_food_x.append(random.randint(0,790))
    snake_food_y.append(random.randint(0,590))
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -snake_distance
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = snake_distance 
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -snake_distance 
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = snake_distance 
                snake_x_change = 0
    snake_x += snake_x_change
    snake_y += snake_y_change
    snake_display.fill(black)
    pygame.draw.rect(snake_display, white, [snake_x, snake_y, snake_size, snake_size])
    for i in range(num_food):
        if clear == True:
            snake_food_x[i] = random.randint(0,790)
            snake_food_y[i] = random.randint(0,590)
            clear == False
        pygame.draw.rect(snake_display, colour, [snake_food_x[i],snake_food_y[i], snake_size, snake_size])
    pygame.display.update()
    clock.tick(snake_speed)