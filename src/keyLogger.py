from pykeyboard import PyKeyboardEvent
class keyLogger(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)
    def tap(self, keycode, character, press):
        print character
    def run(self):
        PyKeyboardEvent.run(self)
