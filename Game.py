from Cell import Cell
from Board import Board


class Game:
    def __init__(self):
        print('Welcome on my minefield')
        self.width = self.console_input('width:')
        self.height = self.console_input('height:')
        self.probability = self.console_input('chances of mine (in range 0-1, gut result with 0.1):','float')
        self.board = Board(width=self.width, height=self.height)
        self.board.set_bombs(self.probability)
        self.state = 'in_game'

    def check(self, x, y):
        board_check = self.board.check(x, y)
        if board_check == 1:
            self.state = 'game_over'
        elif board_check == 0:
            self.state = 'in_game'
        else:
            self.state = 'win'

    def console_input(self, message, form='int'):
        kontroler = False
        while kontroler == False:
            try:
                if form=='str':
                    var = str(input(message))
                elif form=='float':
                    var = float(input(message))
                else:
                    var = int(input(message))
                kontroler = True
            except ValueError:
                print('Error, not accepted format, try again')
        return var


g = Game()
print(g.board.safe_print())
while g.state == 'in_game':
    kontroler = False
    while kontroler == False:
        try:
            x, y = input('coordinates (row column):').split()
            x = int(x) - 1
            if x < 0 or x > g.board.height - 1:
                raise ValueError
            y = int(y) - 1
            if y < 0 or y > g.board.width - 1:
                raise ValueError
            kontroler = True
        except ValueError:
            print('Error, accepted format: "X Y", try again…')
    c = Cell(row=x, column=y, board=g.board)
    c.check()
    print(g.board.safe_print())
    if g.board.to_win == 0:
        print('WINNER')
        exit()
    if g.board.state == 'loser':
        print('ITS OVER')
        g.state = 'loser'
        print(g.board.print())
        exit()
