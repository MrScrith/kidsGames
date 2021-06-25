import pygame
from utils import *
import colorfillsquare

class ColorFill:

    _screen = None
    _js1 = None
    _js2 = None
    _squareList = None

    _pressdict = {1: False, "right": False, "left": False}

    # Set values, height (0), width (0)
    _squarecount = (17, 17)
    _movecount = -1
    _maxmoves = 30

    # Playboard calculations, determined based on screen size.
    _playboard = (0, 0) # size of playboard
    _margins = (0, 0, 0, 0) # margins around game area
    _selectorborder = 0
    _selectorbar = (0, 0, 0, 0)
    _curSelection = 0

    _movesborder = 0
    _movesbar = (0, 0)
    _squaresize = (0, 0)

    _playerCount = 1

    _colorList = (COLORS.RED, COLORS.GREEN, COLORS.YELLOW, COLORS.ORANGE, COLORS.BLUE, COLORS.PURPLE)

    _curColor = COLORS.BLACK
    _nextColor = COLORS.BLACK

    def __init__(self, inscreen, js1, js2):
        self._screen = inscreen

        self._js1 = js1
        self._js2 = js2

        self._squareList = []

        if self._js2 is not None:
            self._playerCount = 2

        # Screen size calculations
        height = self._screen.get_height()
        width = self._screen.get_width()
        self._margins = ((height * 0.05), (width * 0.05), (height * 0.05), (width * 0.05))
        self._selectorborder = self._margins[2]  # for moment same as bottom margin
        self._movesborder = self._margins[3]     # for the moment same as left margin


        tmpheight = (height * 0.9)
        tl = (tmpheight - self._maxmoves - 1) % self._maxmoves
        tmpheight = tmpheight - tl

        self._movesbar = (tmpheight, self._margins[1])

        tmpheight = (height * 0.8)
        tl = tmpheight % self._squarecount[0]  # (0 == height)
        tmpheight = tmpheight - tl

        tmpwidth = (width * 0.8)
        tl = tmpwidth % self._squarecount[1]  # (0 == width)
        tmpwidth = tmpwidth - tl
        self._playboard = (tmpheight, tmpwidth)

        self._squaresize = ((self._playboard[0] / self._squarecount[0]), (self._playboard[1] / self._squarecount[1]))

        # put together the selector bar
        self._selectorbar = (
            (self._margins[3] * 3),
            self._playboard[0] + (self._margins[0] * 2),
            self._playboard[1],
            (height * 0.1))

        # This generates the playing field.
        tmptop = self._margins[0]

        for i in range(0, self._squarecount[0]): # Vertical line
            tmpList = []

            tmpleft = self._margins[3] * 3

            for j in range(0, self._squarecount[1]): # Horizontal line
                tmpList.append(colorfillsquare.ColorFillSquare(tmptop,
                                                               tmpleft,
                                                               self._squaresize[0],
                                                               self._squaresize[1],
                                                               self._colorList))
                tmpleft = tmpleft + self._squaresize[1]
            self._squareList.append(tmpList)
            tmptop = tmptop + self._squaresize[0]

        for i in range(0, self._squarecount[0]): # Vertical line
            for j in range(0, self._squarecount[1]): # Horizontal line
                if i > 0:
                    self._squareList[i][j].square_up = self._squareList[i-1][j]

                if i < self._squarecount[0] - 1:
                    self._squareList[i][j].square_down = self._squareList[i + 1][j]

                if j > 0:
                    self._squareList[i][j].square_right = self._squareList[i][j - 1]

                if j < self._squarecount[1] - 1:
                    self._squareList[i][j].square_left = self._squareList[i][j + 1]

        print("current: " + str(self._curColor))
        print("next: " + str(self._nextColor))
        print("square: " + str(self._squareList[0][0].CurrentColor()))

        self._nextColor = self._squareList[0][0].CurrentColor()
        self._squareList[0][0].SpreadColor(self._curColor, self._nextColor, colorfillsquare.UP)
        self._curColor = self._nextColor

        print("current: " + str(self._curColor))
        print("next: " + str(self._nextColor))
        print("square: " + str(self._squareList[0][0].CurrentColor()))

        self._pressdict[1] = True

    def run(self, events):

        buttonPressTime = 0

        self.drawGame()

        return GAMELIST.FILL

    def drawGame(self):
        # set the background

        self._screen.fill(COLORS.GRAY)
        ###########################################################################
        # draw the move counter
        ###########################################################################
        self._DrawMoveCounter()
        self._DrawPlayBoard()
        self._DrawColorSelector()

        if self._curColor != self._nextColor:
            print("now spreading color " + str(self._nextColor))
            self._squareList[0][0].SpreadColor(self._curColor, self._nextColor, colorfillsquare.UP)
            self._curColor = self._nextColor
            self._movecount += 1

        if self._js1 is not None:
            if self._js1.get_button(1) == 1 and self._pressdict[1] is False:
                self._nextColor = self._colorList[self._curSelection]
                self._pressdict[1] = True
            elif (self._js1.get_button(1) == 0) and (self._pressdict[1]) is True:
                self._pressdict[1] = False

            if (self._js1.get_axis(0).real < -0.1) and (self._pressdict["right"] is False):
                self._pressdict["right"] = True
                self._pressdict["left"] = False
                self._curSelection = self._curSelection - 1
                if self._curSelection < 0:
                    self._curSelection = len(self._colorList) - 1
            elif (self._js1.get_axis(0).real > 0.1) and (self._pressdict["left"] is False):
                self._pressdict["right"] = False
                self._pressdict["left"] = True
                self._curSelection = self._curSelection + 1
                if self._curSelection > len(self._colorList) - 1:
                    self._curSelection = 0
            elif (self._js1.get_axis(0).real < 0.1) and (self._js1.get_axis(0).real > -0.1):
                self._pressdict["right"] = False
                self._pressdict["left"] = False


    def _DrawMoveCounter(self):
        pygame.draw.rect(self._screen,
                         COLORS.WHITE,
                         pygame.Rect(self._margins[3] - 1, self._margins[0] - 1, self._movesbar[1] + 2,
                                     self._movesbar[0] + 2))

        pygame.draw.rect(self._screen,
                         COLORS.BLACK,
                         pygame.Rect(self._margins[3], self._margins[0], self._movesbar[1], self._movesbar[0]))

        trtop = self._margins[0] + 1
        trleft = self._margins[3]
        trwidth = self._movesbar[1]
        trheight = (self._movesbar[0] - self._maxmoves - 1) / self._maxmoves

        for i in range(0, self._maxmoves):

            mvcolor = COLORS.RED
            if self._movecount > i:
                mvcolor = COLORS.GRAY

            pygame.draw.rect(self._screen,
                             mvcolor,
                             pygame.Rect(trleft, trtop, trwidth, trheight))
            trtop = trtop + trheight + 1

    def _DrawColorSelector(self):


        pygame.draw.rect(self._screen,
                         COLORS.BLACK,
                         pygame.Rect((self._selectorbar[0] - 1,
                                      self._selectorbar[1] - 1,
                                      self._selectorbar[2] + 2,
                                      self._selectorbar[3] + 2)))

        trleft = (self._margins[3] * 3)
        trwidth = self._selectorbar[2] / len(self._colorList)

        for i in range(0, len(self._colorList)):

            pygame.draw.rect(self._screen,
                             self._colorList[i],
                             pygame.Rect(trleft, self._selectorbar[1], trwidth, self._selectorbar[3]))

            selringcolor = COLORS.BLACK
            if self._curSelection == i:
                selringcolor = COLORS.WHITE

            pygame.draw.rect(self._screen,
                             selringcolor,
                             pygame.Rect(trleft + 5, self._selectorbar[1] + 5, trwidth - 10, self._selectorbar[3] - 10))

            pygame.draw.rect(self._screen,
                             self._colorList[i],
                             pygame.Rect(trleft + 10, self._selectorbar[1] + 10, trwidth - 20, self._selectorbar[3] - 20))

            trleft = trleft + trwidth

    def _DrawPlayBoard(self):
        pygame.draw.rect(self._screen,
                         COLORS.BLACK,
                         pygame.Rect(
                            (self._margins[3] * 3) - 1,  # left
                            self._margins[0] - 1,        # top
                            self._playboard[1] + 2,      # width
                            self._playboard[0] + 2))     # height

        for i in range(0, self._squarecount[0]): # Vertical line
            for j in range(0, self._squarecount[1]): # Horizontal line
                self._squareList[i][j].DrawSquare(self._screen, 0)



