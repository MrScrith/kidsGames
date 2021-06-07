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
    _color_index = 0
    _curShape = SQUARE
    _size = 10

    _color_list = [BLUE, WHITE, BLACK, RED, YELLOW, GREEN, PINK]

    def get_size(self):
        return self._size

    def change_x(self, value, width):
        self._curX += value

        if self._curX < 0:
            self._curX = 0
        elif self._curX > width - self.get_size():
            self._curX = width - self.get_size()

    def change_y(self, value, height):
        self._curY += value

        if self._curY < 0:
            self._curY = 0
        elif self._curY > height - self.get_size():
            self._curY = height - self.get_size()

    def inc_size(self):
        self._size += 5
        if self._size >= 100:
            self._size = 100

    def dec_size(self):
        self._size -= 5
        if self._size <= 10:
            self._size = 10

    def next_color(self):
        self._color_index += 1
        if self._color_index >= len(self._color_list):
            self._color_index = 0
        self._color = self._color_list[self._color_index]

    def prev_color(self):
        self._color_index -= 1
        if self._color_index == 0:
            self._color_index = len(self._color_list) - 1
        self._color = self._color_list[self._color_index]


    def draw_player(self, surface):
        if self._curShape == SQUARE:
            pygame.draw.rect(surface,
                             self._color,
                             pygame.Rect(self._curX, self._curY, self._size, self._size))

    def __init__(self):
        self.color = RED
        self._curShape = SQUARE
        self._curX = 100
        self._curY = 100

