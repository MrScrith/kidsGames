import sys
import pygame

import player

pygame.init()

GAME = 0
MENU = 1





if __name__ == '__main__':
    pl1 = None
    pl2 = None
    joystick1 = None
    joystick2 = None

    prog_mode = GAME

    screen = pygame.display.set_mode((900, 500))
    #screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

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
        print("Two Joystick found and initialized!")
    elif pygame.joystick.get_count() > 0:
        joystick1 = pygame.joystick.Joystick(0)
        joystick1.init()
        print("One Joystick found and initialized!")
        pl1 = player.Player()
    else:
        print("No joystick.")
    
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
            if event.type == pygame.JOYBUTTONDOWN:
                print(str(joystick.get_button(0)))
                if joystick.get_button(0) == 1:
                    pl.next_color()
                elif joystick.get_button(3) == 1:
                    pl.prev_color()
                elif joystick.get_button(5) == 1:
                    pl.inc_size()
                elif joystick.get_button(4) == 1:
                    pl.dec_size()

def playgame(screen, pl1, pl2, joystick1, joystick2):

    pl1.change_y(joystick1.get_axis(1).real * 5, screen.get_height())

    pl1.change_z(joystick1.get_axis(0).real * 5, screen.get_width())

    pl1.draw_player(screen)

    if joystick2 is not None:
        pl2.change_y(joystick2.get_axis(1).real * 5, screen.get_height())
        pl2.change_z(joystick2.get_axis(0).real * 5, screen.get_width())
        pl2.draw_player(screen)

def menu():
    pass



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
