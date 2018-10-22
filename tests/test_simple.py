from random import seed

from .context import pysweeper
from .core import get_neighbors_test

def test_neighbors_simple():
    seed(0)
    from .boards.simple2 import board
    from .neighbors.simple2 import neighbors
    game = pysweeper.Minesweeper(size=2)
    game.reset()
    assert get_neighbors_test(game) == neighbors
