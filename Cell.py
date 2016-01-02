class Cell:
    neighbours = -1

    def __init__(self, row, column, board):
        if not board.is_on_board(column, row):
            raise ValueError('wrong parameters')
        self.board = board
        self.row = row
        self.column = column
        self.state_on_board = self.board._mapa[self.row][self.column]

    def is_bomb(self):
        if self.state_on_board == -1:
            return True
        return False

    def set_state(self, state):
        self.board.change_value_on_board(column=self.column, row=self.row, value=state)
        self.state_on_board = state

    def calculate_neighbours(self):
        neighbours = 0
        try:
            neighbours += Cell(self.row - 1, self.column - 1, self.board).is_bomb()
        except:
            pass
        try:
            neighbours += Cell(self.row, self.column - 1, self.board).is_bomb()
        except:
            pass
        try:
            neighbours += Cell(self.row + 1, self.column - 1, self.board).is_bomb()
        except:
            pass
        try:
            neighbours += Cell(self.row - 1, self.column, self.board).is_bomb()
        except:
            pass
        try:
            neighbours += Cell(self.row + 1, self.column, self.board).is_bomb()
        except:
            pass
        try:
            neighbours += Cell(self.row - 1, self.column + 1, self.board).is_bomb()
        except:
            pass
        try:
            neighbours += Cell(self.row, self.column + 1, self.board).is_bomb()
        except:
            pass
        try:
            neighbours += Cell(self.row + 1, self.column + 1, self.board).is_bomb()
        except:
            pass
        self.neighbours = neighbours
        return neighbours

    def check(self):
        if self.state_on_board == -1:
            self.set_state(100)
            self.board.state = 'loser'
            return self.state_on_board
        if not self.state_on_board == -2:
            return False
        self.set_state(self.calculate_neighbours())
        self.board.to_win-=1
        if self.state_on_board == 0:
            try:
                Cell(row=self.row - 1, column=self.column - 1, board=self.board).check()
            except:
                pass
            try:
                Cell(row=self.row - 1, column=self.column, board=self.board).check()
            except:
                pass
            try:
                Cell(row=self.row - 1, column=self.column + 1, board=self.board).check()
            except:
                pass
            try:
                Cell(row=self.row, column=self.column - 1, board=self.board).check()
            except:
                pass
            try:
                Cell(row=self.row, column=self.column + 1, board=self.board).check()
            except:
                pass
            try:
                Cell(row=self.row + 1, column=self.column - 1, board=self.board).check()
            except:
                pass
            try:
                Cell(row=self.row + 1, column=self.column, board=self.board).check()
            except:
                pass
            try:
                Cell(row=self.row + 1, column=self.column + 1, board=self.board).check()
            except:
                pass
        return self.state_on_board
