from utils import *
import colorplayer


class ColorMain:

    screen = None
    pl1 = None
    pl2 = None

    def __init__(self, inscreen, js1, js2):
        self.screen = inscreen

        if js1 is not None:
            self.pl1 = colorplayer.ColorPlayer(js1)
        if js2 is not None:
            self.pl2 = colorplayer.ColorPlayer(js1)

    def run(self, events):

        if self.pl1 is not None:
            self.pl1.update_player(self.screen)
            self.pl1.draw_player(self.screen)

        if self.pl2 is not None:
            self.pl2.update_player(self.screen)
            self.pl2.draw_player(self.screen)

        return GAMELIST.DRAW

