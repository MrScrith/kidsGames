
from utils import GAMELIST

class ColorFill:

    _screen = None
    _js1 = None
    _js2 = None

    _playerCount = 1

    def __init__(self, inscreen, js1, js2):
        self._screen = inscreen

        self._js1 = js1
        self._js2 = js2

        if self._js2 is not None:
            self._playerCount = 2

    def run(self, events):

        buttonPressTime = 0

        return GAMELIST.FILL