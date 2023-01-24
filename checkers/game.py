import pygame
from constants.constants import BLACK, WHITE, BLUE, SQUARE_SIZE
from checkers.board import Board


class Game:
    def __init__(self, win):
        self.board = None
        self.turn = None
        self.selected = None
        self.valid_moves = None
        self._init()
        self.win = win
        self.checked = False

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = BLACK
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()

    def select(self, row, col):

        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)

        if piece != 0 and piece.color == self.turn:
            pieces = self.board.get_valid_pieces(piece.color)
            if piece in pieces:
                self.selected = piece
                valid_moves = self.board.get_valid_moves(piece)
                k1 = (0, 0)
                k2 = (0, 0)
                v1 = []
                v2 = []
                counter = 0
                for k in valid_moves:
                    if counter == 0:
                        k1 = k
                        v1 = valid_moves[k1]
                        counter += 1
                    else:
                        k2 = k
                        v2 = valid_moves[k2]

                if len(v1) == len(v2):
                    self.valid_moves = valid_moves
                if len(v1) < len(v2):
                    self.valid_moves = {k2: v2}
                if len(v1) > len(v2):
                    self.valid_moves = {k1: v1}

            return True

        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE,
                               (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()
