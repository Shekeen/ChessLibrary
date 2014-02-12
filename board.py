# -*- coding: utf-8 -*-


class MoveException(Exception):
    pass


class Board:
    ROWS = ('1', '2', '3', '4', '5', '6', '7', '8')
    COLUMNS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

    @classmethod
    def cell_to_coord(cls, cell):
        if len(cell) != 2:
            raise MoveException('Wrong cell format')

        try:
            col_idx = cls.COLUMNS.index(cell[0])
            row_idx = cls.ROWS.index(cell[1])
        except ValueError:
            raise MoveException('Wrong cell format')

        return 8 * row_idx + col_idx

    def __init__(self):
        self.board = [None] * 64

    def get_figure(self, cell):
        return self.board[Board.cell_to_coord(cell)]

    def place_figure(self, cell, figure):
        self.board[Board.cell_to_coord(cell)] = figure

    def remove_figure(self, cell):
        self.board[Board.cell_to_coord(cell)] = None

    def move_figure(self, cell_from, cell_to):
        fig = self.get_figure(cell_from)

        if fig is None:
            raise MoveException('Source cell is empty')
        if self.get_figure(cell_to) is not None:
            raise MoveException('Destination cell is not empty')

        self.remove_figure(cell_from)
        self.place_figure(cell_to, fig)

    def set_figure_placement(self, placement):
        self.clear_board()
        for fig, cell in placement:
            self.place_figure(cell, fig)

    def clear_board(self):
        self.board = [None] * 64
