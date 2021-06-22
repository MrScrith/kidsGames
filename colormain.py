import pygame
import time

import colorplayer

pygame.init()

class ColorMain:

    screen = None
    pl1 = None
    pl2 = None

    def __init__(self, inscreen, js1, js2):
        if inscreen is not None:
            self.screen = inscreen
        else:
            self.screen = pygame.display.set_mode((900, 500))
            #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        if js1 is not None:
            self.pl1 = colorplayer.ColorPlayer(js1)
        if js2 is not None:
            self.pl2 = colorplayer.ColorPlayer(js1)



    def run(self, event):

        buttonPressTime = 0

        if self.pl1 is not None:
            self.pl1.update_player(self.screen)
            self.pl1.draw_player(self.screen)

        if self.pl2 is not None:
            self.pl2.update_player(self.screen)
            self.pl2.draw_player(self.screen)

        for event in pygame.event.get():

            if event.type == pygame.JOYDEVICEADDED:
                if pl1 is None:
                    pl1 = colorplayer.ColorPlayer(pygame.joystick.Joystick(int(event.device_index)))
                elif pl2 is None:
                    pl2 = colorplayer.ColorPlayer(pygame.joystick.Joystick(int(event.device_index)))

if __name__ == '__main__':
    ColorMain(None)

