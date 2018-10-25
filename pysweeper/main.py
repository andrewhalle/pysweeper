from pysweeper.game import Minesweeper

parser = argparse.ArgumentParser(description="play minesweeper!")
parser.add_argument("-n", "--size", action="store",
                    type=int, default=10, help="board size")
args = parser.parse_args()
game = Minesweeper(size=args.size)
while game.play_again:
    game.reset()
    game.play()
