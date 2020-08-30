class Grid:
    def __init__(self, cellLength, screenWidth, screenHeight):
        self.cellLength = cellLength
        self.width = screenWidth / cellLength
        self.height = screenHeight / cellLength
