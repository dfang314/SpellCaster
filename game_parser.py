import letter

def get_game_state(players):
    # TODO
    for player in players:
        player.gems = 4
        player.pts = 10
    grid = []
    for i in range(5):
        grid.append([])
        for j in range(5):
            grid[i].append(letter.Letter("b"))
    return grid, 2, 3
    