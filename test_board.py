from unittest import TestCase
from nose.tools import *
from Board import Board


class TestBoard(TestCase):
    def test___init__(self):
        with self.assertRaises(ValueError):
            Board(-1, 0)
        with self.assertRaises(ValueError):
            Board(0, 0)
        with self.assertRaises(ValueError):
            Board(0, 1)
        with self.assertRaises(ValueError):
            Board(1, 0)
        b = Board(1, 1)
        assert_equal(b._mapa, [[-2]])
        b = Board(2, 2)
        assert_equal(b._mapa, [[-2, -2], [-2, -2]])
        b = Board(2, 1)
        assert_equal(b.height, 1)
        assert_equal(b.width, 2)
        assert_equal(b._mapa, [[-2, -2]])
        b = Board(1, 2)
        assert_equal(b._mapa, [[-2], [-2]])
        assert_equal(b.height, 2)
        assert_equal(b.width, 1)
        assert_equal(b.state, 'empty')

    def test_print(self):
        b = Board(1, 1)
        assert_equal(b.print(), "---\n| |\n---")
        b = Board(1, 2)
        assert_equal(b.print(), "---\n| |\n| |\n---")
        b = Board(2, 1)
        assert_equal(b.print(), "-----\n| | |\n-----")
        b = Board(9, 1)
        b._mapa = [[-2, -1, 100, 1, 2, 3, 4, 5, 6]]
        assert_equal(b.print(), "-------------------\n| |x|!|1|2|3|4|5|6|\n-------------------")

    def test_clear(self):
        b = Board(5, 2)
        b._mapa = [[-2, -1, 100, 1, 2], [1, 1, 1, 1, 1]]
        b.clear()
        assert_equal(b._mapa, [[-2, -2, -2, -2, -2], [-2, -2, -2, -2, -2]])

    def test_set_bombs(self):
        b = Board(5, 2)
        b.set_bombs(0)
        assert_equal(b._mapa, [[-2, -2, -2, -2, -2], [-2, -2, -2, -2, -2]])
        assert_equal(b.state, 'armed')
        b.set_bombs(1)
        assert_equal(b._mapa, [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]])
        assert_equal(b.state, 'armed')

    def test_safe_print(self):
        b = Board(1, 1)
        assert_equal(b.safe_print(), "---\n| |\n---")
        b = Board(1, 2)
        assert_equal(b.safe_print(), "---\n| |\n| |\n---")
        b = Board(2, 1)
        assert_equal(b.safe_print(), "-----\n| | |\n-----")
        b = Board(9, 1)
        b._mapa = [[-2, -1, 100, 1, 2, 3, 4, 5, 6]]
        assert_equal(b.safe_print(), "-------------------\n| | |!|1|2|3|4|5|6|\n-------------------")

    def test_is_on_board(self):
        b = Board(2, 5)
        assert_equal(b.is_on_board(3, 1), False)
        assert_equal(b.is_on_board(1, 1), True)
        assert_equal(b.is_on_board(-1, 0), False)
        assert_equal(b.is_on_board(0, -1), False)
        assert_equal(b.is_on_board(-1, -1), False)
        assert_equal(b.is_on_board(2, 5), False)
        assert_equal(b.is_on_board(1, 4), True)
        assert_equal(b.is_on_board(1, 5), False)
        assert_equal(b.is_on_board(2, 4), False)

    def test_change_value_on_board(self):
        b = Board(5, 2)
        b._mapa = [[-2, -1, 100, 1, 2], [1, 1, 1, 1, 1]]
        b.change_value_on_board(row=1,column=0, value=100)
        assert_equal(b._mapa, [[-2, -1, 100, 1, 2], [100, 1, 1, 1, 1]])
        b._mapa = [[-2, -1, 100, 1, 2], [1, 1, 1, 1, 1]]
        b.change_value_on_board(row=1,column=4, value=100)
        assert_equal(b._mapa, [[-2, -1, 100, 1, 2], [1, 1, 1, 1, 100]])

