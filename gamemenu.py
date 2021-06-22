import pygame

import colorplayer

pygame.init()

GRAY = (120, 120, 120)
YELLOW = (255, 255, 0)
LTBLUE = (120, 120, 255)
BLACK = (0, 0, 0)

POS1 = 50
POS2 = 90
POS3 = 130

class GameMenu:

    screen = None
    js1 = None
    js2 = None
    selected = 0

    textfont = pygame.font.SysFont("Corbel", 20)

    def __init__(self, inscreen, js1, js2):
        self.screen = inscreen
        self.js1 = js1
        self.js2 = js2

    def run(self, event):

        self.screen.fill(GRAY)

        # Drawing game

        self.drawMenuBox(0, "Drawing Game", POS1)
        self.drawMenuBox(1, "Color Fill", POS2)
        self.drawMenuBox(2, "QUIT", POS3)


    def drawMenuBox(self, index, title, position):
        center = self.screen.get_width()/2

        if self.selected == index:
            pygame.draw.rect(self.screen, YELLOW, [center-105, position-15, 210, 30])

        pygame.draw.rect(self.screen, LTBLUE, [center-100, position-10, 200, 20])

        text = self.textfont.render(title, True, BLACK)

        self.screen.blit(text, (center-(text.get_width()/2), position-8))