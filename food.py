import random
import pygame

FOOD_COLOUR = (255, 0, 0)

class FoodManager:
    def __init__(self, screen, grid, snake):
        self.screen = screen
        self.grid = grid
        self.snake = snake
        self.generateFood()
    
    def generateFood(self):
        generated = False
        while not generated:
            xPos = random.randint(0, self.grid.width-1)
            yPos = random.randint(0, self.grid.height-1)

            samePos = False
            for (snakeXPos, snakeYPos) in self.snake.body:
                if (xPos == snakeXPos and yPos == snakeYPos):
                    samePos = True
                    break
            
            if not samePos:
                generated = True
        
        self.food = (xPos, yPos)

    def draw(self):
        screenXPos = self.food[0] * self.grid.cellLength
        screenYPos = self.food[1] * self.grid.cellLength

        pygame.draw.rect(self.screen, FOOD_COLOUR, [screenXPos, screenYPos, self.grid.cellLength, self.grid.cellLength])

    def is_eaten(self):
        if self.snake.body[0][0] == self.food[0] and self.snake.body[0][1] == self.food[1]:
            return True
    
        return False
