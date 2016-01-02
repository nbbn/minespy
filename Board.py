import random
from Cell import Cell


class Board:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError('wrong width or height')
        self._mapa = []
        self.width = width
        self.height = height
        for i in range(height):
            self._mapa.append([])
            for j in range(width):
                self._mapa[i].append(-2)
        self.state = 'empty'
        self.to_win = self.width*self.height

    def change_value_on_board(self, row, column, value):
        self._mapa[row][column] = value

    def print(self):
        to_return = ''
        to_return += (1 + self.width * 2) * '-' + "\n"
        for i in range(self.height):
            to_return += '|'
            for j in range(self.width):
                if self._mapa[i][j] == -2:
                    to_return += ' '
                elif self._mapa[i][j] == -1:
                    to_return += 'x'
                elif self._mapa[i][j] == 100:
                    to_return += '!'
                else:
                    to_return += str(self._mapa[i][j])
                to_return += '|'
            to_return += "\n"
        to_return += (1 + self.width * 2) * '-'
        return to_return

    def clear(self):
        for i in range(self.height):
            for j in range(self.width):
                self._mapa[i][j] = -2
        self.state = 'empty'

    def set_bombs(self, prob):
        for i in range(self.height):
            for j in range(self.width):
                r = random.random()
                if r < prob:
                    self._mapa[i][j] = -1
                    self.to_win -=1
        self.state = 'armed'

    def safe_print(self):
        to_return = ''
        to_return += (1 + self.width * 2) * '-' + "\n"
        for i in range(self.height):
            to_return += '|'
            for j in range(self.width):
                if self._mapa[i][j] == 100:
                    to_return += '!'
                elif self._mapa[i][j] > -1:
                    to_return += str(self._mapa[i][j])
                else:
                    to_return += ' '
                to_return += '|'
            to_return += "\n"
        to_return += (1 + self.width * 2) * '-'
        return to_return

    def is_on_board(self, column, row):
        if column < self.width and column >= 0:
            if row < self.height and row >= 0:
                return True
        return False

