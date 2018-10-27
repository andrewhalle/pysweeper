from random import randint
import sys


class Cell:

    def __init__(self):
        self.has_mine = False
        self.has_flag = False
        self.neighbors_with_mines = None
        self.covered = True

    def _display_value(self):
        if self.covered and self.has_flag:
            return "^"
        elif self.covered:
            return "o"
        elif self.has_mine:
            return "*"
        elif self.neighbors_with_mines == 0:
            return "."
        else:
            return str(self.neighbors_with_mines)

    def _place_mine(self):
        self.has_mine = False

    def _uncover(self):
        self.covered = False

    def _is_safe(self):
        return not self.has_mine



class Minesweeper:

    @staticmethod
    def get_move():
        move = input(">>> ").split()
        if len(move) == 2:
            move = tuple(map(int, move))
        else:
            move = (move[0], int(move[1]), int(move[2]))
        return move

    def __init__(self, size=10):
        self.play_again = True
        self.playing = None
        self.size = size
        self.field = []

    def _get(self, row, col):
        if row >= 0 and row < self.size and col >= 0 and col < self.size:
            return self.field[row*self.size + col]
        else:
            return None

    def _get_neighbors_with_mines(self, row, col):
        neighbors = []
        cell = self._get(row, col)
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if not (i == row and j == col):
                    curr = self._get(i, j)
                    if curr is not None:
                        neighbors.append(curr)
        neighbors_with_mines = 0
        for n in neighbors:
            if n.has_mine:
                neighbors_with_mines += 1
        return neighbors_with_mines

    def _set(self, row, col, val):
        self.field[row*self.size + col] = val

    def reset(self):
        self.playing = None
        self.field = []
        for i in range(self.size**2):
            self.field.append(Cell())
        mines = self.size
        while mines != 0:
            row, col = randint(0, self.size-1), randint(0, self.size-1)
            cell = self._get(row, col)
            if not cell.has_mine:
                cell.has_mine = True
                mines -= 1
        for i in range(self.size):
            for j in range(self.size):
                self._get(i, j).neighbors_with_mines = self._get_neighbors_with_mines(i, j)

    def _uncover(self, row, col):
        cell = self._get(row, col)
        if cell is None or not cell.covered:
            return
        cell.covered = False
        if cell.neighbors_with_mines == 0:
            for i in range(row-1, row+2):
                for j in range(col-1, col+2):
                    self._uncover(i, j)
            
    def _enter(self, move):
        if move[0] == "f":
            cell = self._get(*move[1:])
            cell.has_flag = not cell.has_flag
        else:
            self._uncover(*move)

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

    def _peek(self):
        for i in range(self.size):
            for j in range(self.size):
                cell = self._get(i, j)
                if cell.has_mine:
                    sys.stdout.write("* ")
                else:
                    sys.stdout.write(". ")
            sys.stdout.write("\n")


