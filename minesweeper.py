import argparse
from enum import Enum
from random import randint
import sys


class Cell:

    def __init__(self, val):
        self.val = val
        self.covered = True

    def uncover(self):
        self.covered = False

    def is_safe(self):
        return self.val is CellValue.SAFE


class CellValue(Enum):
    SAFE = 0
    MINE = 1


class Minesweeper:

    @staticmethod
    def get_move():
        input(">>> ")
        return None

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
            self.field.append(Cell(CellValue.SAFE))
        mines = self.size
        while mines != 0:
            row, col = randint(0, self.size-1), randint(0, self.size-1)
            if self._get(row, col).is_safe():
                self._set(row, col, Cell(CellValue.MINE))
                mines -= 1

    def play(self):
        self.playing = True
        while self.playing:
            self.print()
            move = Minesweeper.get_move()
            self.playing = False
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
                if self._get(i, j).is_safe():
                    sys.stdout.write(". ")
                else:
                    sys.stdout.write("* ")
                sys.stdout.write(" ")
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
