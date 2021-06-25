import pygame
import time

from utils import *
import colordraw
import gamemenu
import colorfill

pygame.init()

# Current list of games, more to be added later.
gameList = ["Draw Colors", "Color Fill"]

def Main():
    js1 = None
    js2 = None

    screen = pygame.display.set_mode((900, 500), pygame.DOUBLEBUF, 32)
    #screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN & pygame.DOUBLEBUF, 32)

    clock = pygame.time.Clock()

    gameObj = gamemenu.GameMenu(screen, js1, js2)
    gameMode = GAMELIST.MENU

    buttonPressTime = 0

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
                        gameMode = GAMELIST.MENU
                        del gameObj
                        gameObj = gamemenu.GameMenu(screen, js1, js2)

            if event.type == pygame.JOYBUTTONDOWN:
                print(str(event))
                if event.button == 8:
                    buttonPressTime = time.time()

            if event.type == pygame.JOYDEVICEADDED:
                if js1 is None:
                    js1 = pygame.joystick.Joystick(int(event.device_index))
                elif js2 is None:
                    js2 = pygame.joystick.Joystick(int(event.device_index))

                gameMode = GAMELIST.MENU
                del gameObj
                gameObj = gamemenu.GameMenu(screen, js1, js2)

        # last option
        newMode = gameObj.run(eventList)
        if newMode != gameMode:
            del gameObj
            gameMode = newMode
            screen.fill(COLORS.GRAY) # blank(ish) the screen for the new game.
            if gameMode == GAMELIST.MENU:
                gameObj = gamemenu.GameMenu(screen, js1, js2)
            elif gameMode == GAMELIST.DRAW:
                gameObj = colordraw.ColorDraw(screen, js1, js2)
            elif gameMode == GAMELIST.FILL:
                gameObj = colorfill.ColorFill(screen, js1, js2)
            elif gameMode == GAMELIST.QUIT:
                run = False


    pygame.quit()




if __name__ == '__main__':
    Main()

