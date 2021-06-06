import pygame
SQUARE = 0
CIRCLE = 1

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PINK = (255, 125, 125)

class Player:
    _color = BLUE
    _curShape = SQUARE


    def draw_player(self, surface):
        if self._curShape == SQUARE:
            pygame.draw.rect(surface,
                             self._color,
                             pygame.Rect(self._curX, self._curY, 10, 10))

    def __init__(self):
        self.color = RED
        self._curShape = SQUARE
        self._curX = 100
        self._curY = 100

