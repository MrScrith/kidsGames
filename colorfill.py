
from utils import GAMELIST

class ColorFill:

    _screen = None
    _js1 = None
    _js1 = None

    def __init__(self, inscreen, js1, js2):
        self._screen = inscreen

        self._js1 = js1
        self._js2 = js2

    def run(self, events):

        buttonPressTime = 0

        return GAMELIST.FILL