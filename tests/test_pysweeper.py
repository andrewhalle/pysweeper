from .context import pysweeper


def test_creation():
    game = pysweeper.Minesweeper()
    assert game is not None


