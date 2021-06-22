import pygame
import sys
SQUARE = 0
CIRCLE = 1

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PINK = (255, 125, 125)


class ColorPlayer:
    _color = BLUE
    _color_index = 0
    _curShape = SQUARE
    _size = 10
    _js = None
    _active = False

    _color_list = [BLUE, WHITE, BLACK, RED, YELLOW, GREEN, PINK]

    _press_list = {0: False, 1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False}

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
        if self._color_index < 0:
            self._color_index = len(self._color_list) - 1
        self._color = self._color_list[self._color_index]

    def draw_player(self, surface):
        if self._active:
            if self._curShape == SQUARE:
                pygame.draw.rect(surface,
                                 self._color,
                                 pygame.Rect(self._curX, self._curY, self._size, self._size))
            elif self._curShape == CIRCLE:
                pygame.draw.circle(surface,
                                 self._color,
                                   (self._curX + self._size / 2, self._curY + self._size / 2),
                                   self._size/2)

    def update_player(self, screen):
        if self._js.get_button(1) == 1 and self._press_list[1] is False:
            if self._curShape == SQUARE:
                self._curShape = CIRCLE
            else:
                self._curShape = SQUARE
            self._press_list[1] = True
        elif self._js.get_button(1) == 0 and self._press_list[1] is True:
            self._press_list[1] = False

        if self._js.get_button(2) == 1 and self._press_list[2] is False:
            if self._curShape == SQUARE:
                self._curShape = CIRCLE
            else:
                self._curShape = SQUARE
            self._press_list[2] = True
        elif self._js.get_button(2) == 0 and self._press_list[2] is True:
            self._press_list[2] = False

        if self._js.get_button(0) == 1 and self._press_list[0] is False:
            self.next_color()
            self._press_list[0] = True
            print("0 pressed")
        elif self._js.get_button(0) == 0 and self._press_list[0] is True:
            self._press_list[0] = False
            print("0 up")

        if self._js.get_button(3) == 1 and self._press_list[3] is False:
            self.prev_color()
            self._press_list[3] = True
            print("3 pressed")
        elif self._js.get_button(3) == 0 and self._press_list[3] is True:
            self._press_list[3] = False
            print("3 up")

        if self._js.get_button(5) == 1 and self._press_list[5] == False:
            self.inc_size()
            self._press_list[5] = True
        elif self._js.get_button(5) == 0 and self._press_list[5] == True:
            self._press_list[5] = False

        if self._js.get_button(4) == 1 and self._press_list[4] == False:
            self.dec_size()
            self._press_list[4] = True
        elif self._js.get_button(4) == 0 and self._press_list[4] == True:
            self._press_list[4] = False

        if self._js.get_button(9) == 1 and self._press_list[9] == False:
            self._active = not self._active
            self._press_list[9] = True
        elif self._js.get_button(9) == 0 and self._press_list[9] == True:
            self._press_list[9] = False

        if "win" in sys.platform:
            self.change_y(self._js.get_axis(4).real * 5, screen.get_height())
            self.change_x(self._js.get_axis(0).real * 5, screen.get_width())
        elif "linux" in sys.platform:
            self.change_y(self._js.get_axis(1).real * 5, screen.get_height())
            self.change_x(self._js.get_axis(0).real * 5, screen.get_width())


    def __init__(self, joystick):
        self.color = RED
        self._curShape = SQUARE
        self._curX = 100
        self._curY = 100
        self._js = joystick
        self._active = False

