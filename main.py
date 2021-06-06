import sys
import pygame

import player

pygame.init()







if __name__ == '__main__':

    pl = player.Player()

    screen = pygame.display.set_mode((900, 500))

    clock = pygame.time.Clock()

    font = pygame.font.SysFont("arial", 16)
    font_height = font.get_linesize()
    event_text = []

    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        print("Joystick found and initialized!")
        print("There are " + str(joystick.get_numaxes()) + " axes,")
        print("There are " + str(joystick.get_numbuttons()) + " buttons,")
        print("There are " + str(joystick.get_numhats()) + " hats on this joystick")
    else:
        print("No joystick.")
    newX = 0
    newY = 0
    
    run = True
    while run:

        pygame.display.update()

        clock.tick(60)

        newX = (joystick.get_axis(0).real * 5) + newX
        newY = (joystick.get_axis(1).real * 5) + newY

        pl._curX = newX
        pl._curY = newY


        pl.draw_player(screen)



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









# See PyCharm help at https://www.jetbrains.com/help/pycharm/
