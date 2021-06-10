import sys
import pygame

import player

pygame.init()

GAME = 0
MENU = 1

def menu():
    pass

def playgame(screen, pl1, pl2, joystick1, joystick2):

    if pl1 is not None:
        pl1.update_player(joystick1, screen)
        pl1.draw_player(screen)

    if pl2 is not None:
        pl2.update_player(joystick2, screen)
        pl2.draw_player(screen)

def main():
    pl1 = None
    pl2 = None
    joystick1 = None
    joystick2 = None

    prog_mode = GAME

    #screen = pygame.display.set_mode((900, 500))
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    clock = pygame.time.Clock()

    font = pygame.font.SysFont("arial", 16)
    font_height = font.get_linesize()
    event_text = []

    if pygame.joystick.get_count() > 1:
        joystick1 = pygame.joystick.Joystick(0)
        joystick1.init()
        pl1 = player.Player()
        joystick2 = pygame.joystick.Joystick(1)
        joystick2.init()
        pl2 = player.Player()
        print("Two Joysticks found and initialized!")
    elif pygame.joystick.get_count() > 0:
        joystick1 = pygame.joystick.Joystick(0)
        joystick1.init()
        print("One Joystick found and initialized!")
        pl1 = player.Player()
    else:
        print("No joystick.")

    print("Joystick found and initialized!")
    print("There are " + str(joystick1.get_numaxes()) + " axes,")
    print("There are " + str(joystick1.get_numbuttons()) + " buttons,")
    print("There are " + str(joystick1.get_numhats()) + " hats on this joystick")


    run = True
    while run:

        pygame.display.update()

        clock.tick(60)

        if prog_mode == GAME:
            playgame(screen, pl1, pl2, joystick1, joystick2)
        elif prog_mode == MENU:
            menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type in (pygame.JOYBALLMOTION, pygame.JOYHATMOTION, pygame.JOYBUTTONDOWN, pygame.JOYBUTTONUP):
                print(str(event))
                if joystick1.get_button(8) == 1:
                    run = False
                    pygame.quit()

    pygame.quit()

if __name__ == '__main__':
    main()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
