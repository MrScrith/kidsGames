import sys
import pygame
import time

import colorplayer

pygame.init()

def ColorMain(inscreen):
    pl1 = None
    pl2 = None

    if inscreen is not None:
        screen = inscreen
    else:
        screen = pygame.display.set_mode((900, 500))
        #screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    clock = pygame.time.Clock()

    buttonPressTime = 0

    run = True
    while run:

        pygame.display.update()

        clock.tick(60)

        if pl1 is not None:
            pl1.update_player(screen)
            pl1.draw_player(screen)

        if pl2 is not None:
            pl2.update_player(screen)
            pl2.draw_player(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.JOYBUTTONUP:
                # If the "start" button is pressed for more than 2 seconds quit game.
                if event.button == 8:
                    if time.time() - buttonPressTime > 2:
                        pygame.quit()
                        run = False

            if event.type == pygame.JOYBUTTONDOWN:
                print(str(event))
                if event.button == 8:
                    buttonPressTime = time.time()


            if event.type == pygame.JOYDEVICEADDED:
                if pl1 is None:
                    pl1 = colorplayer.ColorPlayer(pygame.joystick.Joystick(int(event.device_index)))
                elif pl2 is None:
                    pl2 = colorplayer.ColorPlayer(pygame.joystick.Joystick(int(event.device_index)))
    pygame.quit()

if __name__ == '__main__':
    ColorMain(None)

