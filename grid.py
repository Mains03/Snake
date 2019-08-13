class Grid:
    def __init__(self, pixelsPerCubeSide, screenWidth, screenHeight):
        self.pixelsPerCubeSide = pixelsPerCubeSide
        self.width = screenWidth / pixelsPerCubeSide
        self.height = screenHeight / pixelsPerCubeSide