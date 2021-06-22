import pygame
import time

import colormain
import gamemenu

pygame.init()

MENU = 0
DRAW = 1
FILL = 2
QUIT = 99

# Current list of games, more to be added later.
gameList = ["Draw Colors", "Color Fill"]

def Main():
    js1 = None
    js2 = None

    screen = pygame.display.set_mode((900, 500))
    #screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    clock = pygame.time.Clock()

    gameObj = gamemenu.GameMenu(screen, js1, js2)

    run = True
    while run:

        eventList = pygame.event.get()

        pygame.display.update()

        clock.tick(60)

        for event in eventList:
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.JOYBUTTONUP:
                # If the "start" button is pressed for more than 2 seconds quit game.
                if event.button == 8:
                    if time.time() - buttonPressTime > 2:
                        gameMode = MENU
                        del gameObj

            if event.type == pygame.JOYBUTTONDOWN:
                print(str(event))
                if event.button == 8:
                    buttonPressTime = time.time()

            if event.type == pygame.JOYDEVICEADDED:
                if js1 is None:
                    js1 = pygame.joystick.Joystick(int(event.device_index))
                elif js2 is None:
                    js2 = pygame.joystick.Joystick(int(event.device_index))

        # last option
        if not gameObj.run(eventList):
            del gameObj
            gameObj = gamemenu.GameMenu(screen, js1, js2)

    pygame.quit()




if __name__ == '__main__':
    Main()

