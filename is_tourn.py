
class Tourn:
    def __init__(self):
        self.turn  = 'X'

    def new_turn(self):

        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'
