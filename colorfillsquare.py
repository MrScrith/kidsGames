import pygame
from utils import *
from random import randint

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class ColorFillSquare():
    _top = 0
    _left = 0
    _height = 0
    _width = 0
    _currentColor = COLORS.GREEN
    _nextColor = COLORS.GREEN
    square_up = None
    square_right = None
    square_down = None
    square_left = None

    def __init__(self, top, left, height, width, colorlist):
        self._top = top
        self._left = left
        self._height = height
        self._width = width
        self._nextColor = colorlist[ randint(0, len(colorlist)-1)]
        self._currentColor = self._nextColor

    def CurrentColor(self):
        return self._currentColor

    def NextColor(self):
        return self._nextColor

    def SpreadColor(self, selectedcolor, nextcolor, fromsquare):
        if self._currentColor == selectedcolor:
            self._nextColor = nextcolor
            if self.square_up is not None and fromsquare != UP:
                if self.square_up.CurrentColor() == selectedcolor and self.square_up.NextColor() != nextcolor:
                    self.square_up.SpreadColor(selectedcolor, nextcolor, DOWN)
            if self.square_right is not None and fromsquare != RIGHT:
                if self.square_right.CurrentColor() == selectedcolor and self.square_right.NextColor() != nextcolor:
                    self.square_right.SpreadColor(selectedcolor, nextcolor, LEFT)
            if self.square_down is not None and fromsquare != DOWN:
                if self.square_down.CurrentColor() == selectedcolor and self.square_down.NextColor() != nextcolor:
                    self.square_down.SpreadColor(selectedcolor, nextcolor, UP)
            if self.square_left is not None and fromsquare != LEFT:
                if self.square_left.CurrentColor() == selectedcolor and self.square_left.NextColor() != nextcolor:
                    self.square_left.SpreadColor(selectedcolor, nextcolor, RIGHT)

    def DrawSquare(self, screen, transparency):
        # eventually I will do some sort of color tranform, for now...
        self._currentColor = self._nextColor
        pygame.draw.rect(screen,
                         self._currentColor,
                         pygame.Rect(self._left, self._top, self._width, self._height))


