import pygame

SNAKE_COLOUR = (0, 255, 0)
SNAKE_GROWTH_RATE = 2

DIRECTION_UP    = (0, -1)
DIRECTION_DOWN  = (0, 1)
DIRECTION_LEFT  = (-1, 0)
DIRECTION_RIGHT = (1, 0)

class Snake:
    def __init__(self, screen, grid):
        self.screen = screen
        self.grid = grid

		# Head is stored at the front
        self.body = [[grid.width//2-1, grid.height//2]]
        self.newBodyPiece = 0
        self.direction = DIRECTION_RIGHT

    def draw(self):
        for i in range(len(self.body)):
            screenXPos = self.body[i][0] * self.grid.cellLength
            screenYPos = self.body[i][1] * self.grid.cellLength

            pygame.draw.rect(self.screen, SNAKE_COLOUR, [screenXPos, screenYPos, self.grid.cellLength, self.grid.cellLength])

    def move(self):
    	# Add extra body piece
        if self.newBodyPiece > 0:
            lastPos = self.body[len(self.body)-1].copy()
            self.body.append(lastPos)
            self.newBodyPiece -= 1
         
        # Move the body pieces
        for i in range(len(self.body)-1, 0, -1):
            self.body[i][0] = self.body[i-1][0]
            self.body[i][1] = self.body[i-1][1]

		# Move the head
        self.body[0][0] += self.direction[0]
        self.body[0][1] += self.direction[1]

    def left(self):
        if (self.direction != DIRECTION_RIGHT):
            self.direction = DIRECTION_LEFT
    
    def right(self):
        if (self.direction != DIRECTION_LEFT):
            self.direction = DIRECTION_RIGHT
    
    def up(self):
        if (self.direction != DIRECTION_DOWN):
            self.direction = DIRECTION_UP
    
    def down(self):
        if (self.direction != DIRECTION_UP):
            self.direction = DIRECTION_DOWN

    def hitWall(self):
        if self.body[0][0] == -1:
            self.body[0][0] = 0
            return True
        elif self.body[0][0] == self.grid.width:
            self.body[0][0] = self.grid.width -1
            return True
        elif self.body[0][1] == -1:
            self.body[0][1] = 0
            return True
        elif self.body[0][1] == self.grid.height:
            self.body[0][1] = self.grid.height -1
            return True
            
        return False

    def hitBody(self):
        headPos = self.body[0]

        for i in range(1, len(self.body)):
            if headPos[0] == self.body[i][0] and headPos[1] == self.body[i][1]:
                return True

        return False

    def reset(self):
        self.direction = DIRECTION_RIGHT
        self.body = [[self.grid.width // 2, self.grid.height // 2]]
        self.addBody()
    
    def addBody(self):
        self.newBodyPiece = SNAKE_GROWTH_RATE
