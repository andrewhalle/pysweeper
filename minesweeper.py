import argparse
from enum import Enum
from random import randint
import sys


class Cell:

    def __init__(self, field):
        self.has_mine = False
        self.has_flag = False
        self.mine_neighbors = None
        self.covered = True
        self.field = field

    def _calc_mine_neighbors(self):
        self.mine_neighors = 0

    def _display_value(self):
        if self.mine_neighbors is None:
            self._calc_mine_neighbors()
        if self.covered and self.has_flag:
            return "^"
        elif self.covered:
            return "o"
        elif self.has_mine:
            return "*"
        elif self.mine_neighbors == 0:
            return "."
        else:
            return str(self.mine_neighbors)

    def _place_mine(self):
        self.has_mine = False

    def _uncover(self):
        self.covered = False

    def _is_safe(self):
        return not self.has_mine



class Minesweeper:

    @staticmethod
    def get_move():
        move = input(">>> ")
        move = tuple(map(int, move.split()))
        return move

    def __init__(self, args):
        self.play_again = True
        self.playing = None
        self.size = args.size
        self.field = []

    def _get(self, row, col):
        return self.field[row*self.size + col]

    def _set(self, row, col, val):
        self.field[row*self.size + col] = val

    def reset(self):
        self.playing = None
        self.field = []
        for i in range(self.size**2):
            self.field.append(Cell(self.field))
        mines = self.size
        while mines != 0:
            row, col = randint(0, self.size-1), randint(0, self.size-1)
            cell = self._get(row, col)
            if cell._is_safe():
                cell._place_mine()
                mines -= 1

    def _enter(self, move):
        self._get(*move)._uncover()

    def _check_win(self):
        return None

    def play(self):
        self.playing = True
        while self.playing:
            self.print()
            move = Minesweeper.get_move()
            self._enter(move)
            self._check_win()
        self.ask_play_again()

    def ask_play_again(self):
        play_again = input("Play again (y/n)? ")
        if play_again == "y" or play_again == "Y":
            self.play_again = True
        else:
            self.play_again = False
        print("")

    def print(self):
        for i in range(self.size):
            for j in range(self.size):
                sys.stdout.write(self._get(i, j)._display_value() + " ")
            sys.stdout.write("\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="play minesweeper!")
    parser.add_argument("-n", "--size", action="store",
            type=int, default=10, help="board size")
    args = parser.parse_args()
    game = Minesweeper(args)
    while game.play_again:
        game.reset()
        game.play()
