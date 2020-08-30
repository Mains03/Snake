import pygame
import snake
import grid
import food

pygame.init()

dimensions = (640, 480)

screen = pygame.display.set_mode((dimensions[0], dimensions[1]))
pygame.display.set_caption("Snake")

background_colour = (255,255,255)
screen.fill(background_colour)

grid = grid.Grid(20, dimensions[0], dimensions[1])
snake = snake.Snake(screen, grid)
snake.addBody()
food = food.FoodManager(screen, grid, snake)

clock = pygame.time.Clock()

alive = False

running = True
while running:
    screen.fill(background_colour)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if alive:
                if event.key == pygame.K_UP:
                    snake.up()
                elif event.key == pygame.K_DOWN:
                    snake.down()
                elif event.key == pygame.K_LEFT:
                    snake.left() 
                elif event.key == pygame.K_RIGHT:
                    snake.right()
            else:
                if event.key == pygame.K_RETURN:
                    alive = True
                    snake.reset()
                    food.generateFood()

    if alive:
        snake.move()

        if snake.hitWall():
            alive = False
        elif snake.hitBody():
            alive = False
            
        if food.is_eaten():
            snake.addBody()
            food.generateFood()

    food.draw()
    snake.draw()

    pygame.display.update()

    clock.tick(9)

pygame.quit()
