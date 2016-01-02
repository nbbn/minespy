from unittest import TestCase
from nose.tools import *
from Board import Board
from Cell import Cell


class TestCell(TestCase):
    def test___init__(self):
        b = Board(1, 2)
        with self.assertRaises(ValueError):
            Cell(column=1, row=1, board=b)
        b = Board(1, 2)
        with self.assertRaises(ValueError):
            Cell(column=1, row=2, board=b)
        b = Board(1, 2)
        with self.assertRaises(ValueError):
            Cell(column=-1, row=-1, board=b)
        b = Board(1, 2)
        c = Cell(column=0, row=1, board=b)
        assert_equal(c.board, b)

        b = Board(1, 2)
        c = Cell(column=0, row=1, board=b)
        assert_equal(c.row, 1)

        b = Board(1, 2)
        c = Cell(column=0, row=1, board=b)
        assert_equal(c.column, 0)

        b = Board(1, 2)
        c = Cell(column=0, row=1, board=b)
        assert_equal(c.state_on_board, -2)

        b = Board(5, 2)
        b._mapa = [[8, -2, -2, -2, -2], [-2, -2, 100, -2, -2]]
        c = Cell(column=0, row=0, board=b)
        assert_equal(c.state_on_board, 8)

        c = Cell(column=2, row=1, board=b)
        assert_equal(c.state_on_board, 100)

    def test_is_bomb(self):
        b = Board(5, 2)
        b._mapa = [[100, -2, -2, -2, -2], [-2, -1, 100, -2, -2]]
        c = Cell(column=0, row=0, board=b)
        assert_equal(c.is_bomb(), False)
        c = Cell(column=1, row=0, board=b)
        assert_equal(c.is_bomb(), False)
        c = Cell(column=1, row=1, board=b)
        assert_equal(c.is_bomb(), True)

    def test_calculate_neighbours(self):
        b = Board(5, 3)
        b._mapa = [[100, -1, -1, -1, -2], [-2, -1, 100, -1, -1], [-2, -1, -1, -1, 0]]
        c = Cell(column=0, row=0, board=b)
        assert_equal(c.calculate_neighbours(),2)
        assert_equal(c.neighbours, 2)
        c = Cell(column=0, row=2, board=b)
        assert_equal(c.calculate_neighbours(),2)
        assert_equal(c.neighbours, 2)
        c = Cell(column=2, row=1, board=b)
        assert_equal(c.calculate_neighbours(),8)
        assert_equal(c.neighbours, 8)
        c = Cell(column=4, row=0, board=b)
        assert_equal(c.calculate_neighbours(),3)
        assert_equal(c.neighbours, 3)

    def test_set_state(self):
        b = Board(5, 3)
        b._mapa = [[100, -1, -1, -1, -2], [-2, -1, 100, -1, -1], [-2, -1, -1, -1, 0]]
        c = Cell(column=0, row=0, board=b)
        c.set_state(10)
        assert_equal(b._mapa, [[10, -1, -1, -1, -2], [-2, -1, 100, -1, -1], [-2, -1, -1, -1, 0]])
        assert_equal(c.state_on_board, 10)

        b._mapa = [[100, -1, -1, -1, -2], [-2, -1, 100, -1, -1], [-2, -1, -1, -1, 0]]
        c = Cell(column=2, row=2, board=b)
        c.set_state(7)
        assert_equal(b._mapa, [[100, -1, -1, -1, -2], [-2, -1, 100, -1, -1], [-2, -1, 7, -1, 0]])
        assert_equal(c.state_on_board, 7)

    def test_check(self):
        b = Board(5, 2)
        b._mapa = [[-1, -2, -2, -2, -2], [-2, -2, -2, -2, -2]]
        c = Cell(column=0, row=0, board=b)
        returned = c.check()
        assert_equal(b.state, 'loser')
        assert_equal(c.state_on_board, 100)
        assert_equal(b._mapa[c.row][c.column], 100)
        assert_equal(returned, 100)

        b = Board(5, 2)
        b._mapa = [[100, -2, -2, -2, -2], [-2, -2, -2, -2, -2]]
        c = Cell(column=0, row=0, board=b)
        assert_true(not c.check())

        b = Board(5, 2)
        b._mapa = [[5, -2, -2, -2, -2], [-2, -2, -2, -2, -2]]
        c = Cell(column=0, row=0, board=b)
        assert_true(not c.check())

        b = Board(5, 2)
        b._mapa = [[-2, -2, -2, -2, -2], [-2, -2, -2, -2, -2]]
        c = Cell(column=0, row=0, board=b)
        assert_equal(c.check(),0)
        assert_equal(b._mapa, [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

        b = Board(5, 2)
        b._mapa = [[-2, -2, -2, -2, -2], [-2, -2, -2, -2, -1]]
        c = Cell(column=0, row=0, board=b)
        assert_equal(c.check(),0)
        assert_equal(b._mapa, [[0, 0, 0, 1, -2], [0, 0, 0, 1, -1]])

        b = Board(5, 2)
        b._mapa = [[-2, -2, -2, -2, -2], [-2, -2, -2, -2, -1]]
        c = Cell(column=3, row=1, board=b)
        assert_equal(c.check(),1)
        assert_equal(b._mapa, [[-2, -2, -2, -2, -2], [-2, -2, -2, 1, -1]])