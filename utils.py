from enum import IntEnum, auto


class GAMELIST(IntEnum):
    MENU = auto()
    DRAW = auto()
    FILL = auto()
    QUIT = auto()


class COLORS():
    GRAY = (120, 120, 120)
    YELLOW = (255, 255, 0)
    LTBLUE = (120, 120, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    PINK = (255, 125, 125)

    color_list = [BLUE, WHITE, BLACK, RED, YELLOW, GREEN, PINK, LTBLUE]