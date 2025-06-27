import letter
from PIL import Image as im
from imgs import generate_subimg as gen
from imgs import gem_cnn
from imgs import letter_cnn
from tensorflow import keras
import tensorflow as tf

gem_model = None
letter_model = None

def parse_letter(img):
    gem_img = tf.expand_dims(keras.utils.img_to_array(gen.generate_gem_img(img)), 0)
    letter_img = tf.expand_dims(keras.utils.img_to_array(img), 0)

    global gem_model, letter_model
    # based on letter image, figures out whether there is double points,
    # location of dl, location of tl,
    # the letter, and whether there is a gem
    if gem_model is None:
        gem_model = gem_cnn.load_model()
    return False, False, False, tf.squeeze(gem_model(gem_img)).numpy() > 0.5, "a"
    # if letter_model is None:
    #     letter_model = letter_cnn.load_model()
    # return False, False, False, gem_model(gem_img), letter_model(letter_img) # TODO

# returns grid, turn, round, double location, dl location, tl location
# updates players gems and pts
def get_game_state(players):
    # most of the values here are handset
    # TODO
    img = im.open("test.png")
    img = img.resize((550, 500))
    grid_img = img.crop((20, 90, 335, 405))
    players_img = img.crop((370, 0, 540, 499)) # TODO: height needs adjustment for 4 players
    # grid_img.show()
    grid = []
    dl_loc = (-1, -1)
    tl_loc = (-1, -1)
    double_loc = (-1, -1)
    for i in range(5):
        grid.append([])
        for j in range(5):
            # grid is 315x315, we need to see more than just our letter (just to be safe)
            crop_left = j * 60
            crop_right = crop_left + 74
            crop_top = i * 60
            crop_bot = crop_top + 74
            letter_img = grid_img.crop((crop_left, crop_top, crop_right, crop_bot))
            # letter_img.save(f"letter_imgs/{i}_{j}.png")
            dl, tl, double, gem, ch = parse_letter(letter_img)
            # print("GEM", gem)
            # print("CH", ch)
            grid[i].append(letter.Letter(ch))
            grid[i][j].gem = gem

            if dl:
                dl_loc = (i, j)
            if tl:
                tl_loc = (i, j)
            if double:
                double_loc = (i, j)
                

    for player in players:
        player.gems = 4
        player.pts = 10
    
    return grid, 2, 3, double_loc, dl_loc, tl_loc
    