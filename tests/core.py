def get_neighbors_test(game):
    neighbors = ""
    for i in range(game.size):
        for j in range(game.size):
            neighbors += str(game._get(i, j).neighbors_with_mines) + " "
        neighbors += "\n"
    return neighbors
