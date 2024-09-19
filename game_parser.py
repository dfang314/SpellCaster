import letter
from PIL import Image as im

# returns grid, turn, round and updates players gems and pts
def get_game_state(players):
    # TODO
    img = im.open("input.png")
    img = img.resize((550, 500)) # from hand testing we want around 550, 500
    grid_img = img.crop((20, 90, 335, 405)) # hand set
    players_img = img.crop((370, 0, 540, 499)) # TODO: height needs adjustment for 4 players
    for player in players:
        player.gems = 4
        player.pts = 10
    grid = []
    for i in range(5):
        grid.append([])
        for j in range(5):
            grid[i].append(letter.Letter("b"))
    return grid, 2, 3
    