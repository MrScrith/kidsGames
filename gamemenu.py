import pygame
import sys

from utils import *

pygame.init()

GRAY = (120, 120, 120)
YELLOW = (255, 255, 0)
LTBLUE = (120, 120, 255)
BLACK = (0, 0, 0)

# First position is "menu", so drop them back a hair
POS = (0, 50, 90, 130, 170, 210, 250, 290, 330, 370) # expand as needed.

class GameMenu:
    _pressdict = {0: False, 1: False, "up": False, "down": False}

    _screen = None
    _js1 = None
    _js2 = None
    _selected = 2

    _textfont = pygame.font.SysFont("Corbel", 20)

    def __init__(self, inscreen, js1, js2):
        self._screen = inscreen
        self._js1 = js1
        self._js2 = js2
        print("Menu init")

    def run(self, events):

        self._screen.fill(GRAY)

        retval = GAMELIST.MENU

        # Drawing game
        print("selected: " + str(self._selected))
        self.drawMenuBox(GAMELIST.DRAW, "Drawing Game")
        self.drawMenuBox(GAMELIST.FILL, "Color Fill")
        self.drawMenuBox(GAMELIST.QUIT, "QUIT")


        if self._js1 is not None:
            if self._js1.get_button(0) == 1 and self._pressdict[0] is False:
                retval = self._selected
                self._pressdict[0] = True
            elif (self._js1.get_button(0) == 0) and (self._pressdict[0]) is True:
                self._pressdict[0] = False

            if self._js1.get_button(1) == 1 and self._pressdict[1] is False:
                retval = self._selected
                self._pressdict[1] = True
            elif (self._js1.get_button(1) == 0) and (self._pressdict[1]) is True:
                self._pressdict[1] = False

            if "win" in sys.platform:
                if (self._js1.get_axis(4).real < -0.1) and (self._pressdict["up"] is False):
                    self._pressdict["up"] = True
                    self._pressdict["down"] = False
                    self._selected = self._selected - 1
                    if self._selected < 2:
                        self._selected = GAMELIST.QUIT
                elif (self._js1.get_axis(4).real > 0.1) and (self._pressdict["down"] is False):
                    self._pressdict["up"] = False
                    self._pressdict["down"] = True
                    self._selected = self._selected + 1
                    if self._selected > GAMELIST.QUIT:
                        self._selected = 2
                elif (self._js1.get_axis(4).real < 0.1) and (self._js1.get_axis(4).real > -0.1):
                    self._pressdict["up"] = False
                    self._pressdict["down"] = False
            elif "linux" in sys.platform:
                if (self._js1.get_axis(0).real > 0.1) and (self._pressdict["up"] is False):
                    self._pressdict["up"] = True
                    self._pressdict["down"] = False
                    self._selected = self._selected - 1
                    if self._selected < 2:
                        self._selected = GAMELIST.QUIT
                elif (self._js1.get_axis(0).real < -0.1) and (self._pressdict["down"] is False):
                    self._pressdict["up"] = False
                    self._pressdict["down"] = True
                    self._selected = self._selected + 1
                    if self._selected > GAMELIST.QUIT:
                        self._selected = 2
                elif (self._js1.get_axis(0).real < 0.1) and (self._js1.get_axis(0).real > -0.1):
                    self._pressdict["up"] = False
                    self._pressdict["down"] = False

        return retval


    def drawMenuBox(self, index, title):
        center = self._screen.get_width() / 2

        if self._selected == index:
            pygame.draw.rect(self._screen, YELLOW, [center - 105, POS[index] - 15, 210, 30])

        pygame.draw.rect(self._screen, LTBLUE, [center - 100, POS[index] - 10, 200, 20])

        text = self._textfont.render(title, True, BLACK)

        self._screen.blit(text, (center - (text.get_width() / 2), POS[index] - 8))