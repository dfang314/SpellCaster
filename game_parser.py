import letter
import numpy as np
from PIL import Image as im

def parse_letter(img):
    # based on letter image, figures out whether dl or tl is applicable,
    # the letter, whether there is double points, and whether there is a gem
    return False, False, False, False, [0.01] * 26 # TODO

# returns grid, turn, round and updates players gems and pts
def get_game_state(players):
    # most of the values here are handset
    # TODO
    img = im.open("input.png")
    img = img.resize((550, 500))
    grid_img = img.crop((20, 90, 335, 405))
    players_img = img.crop((370, 0, 540, 499)) # TODO: height needs adjustment for 4 players
    # grid_img.show()
    grid = []
    for i in range(5):
        grid.append([])
        for j in range(5):
            # grid is 315x315, we need to see more than just our letter (just to be safe)
            crop_left = j * 60
            crop_right = crop_left + 74
            crop_top = i * 60
            crop_bot = crop_top + 74
            letter_img = grid_img.crop((crop_left, crop_top, crop_right, crop_bot))
            letter_img.save(f"letter_imgs/{i}_{j}.png")
            dl, tl, double, gem, letter_probs = parse_letter(letter_img)
            best_letter = chr(ord("a") + np.argmax(letter_probs))
            grid[i].append(letter.Letter(best_letter))
            grid[i][j].dl = dl
            grid[i][j].tl = tl
            grid[i][j].double = double
            grid[i][j].gem = gem

    for player in players:
        player.gems = 4
        player.pts = 10
    
    return grid, 2, 3
    