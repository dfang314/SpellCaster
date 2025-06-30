import letter
from PIL import Image as im
from imgs import generate_subimg as gen
from imgs import gem_cnn
from imgs import letter_cnn
from tensorflow import keras
import tensorflow as tf


def parse_letter(img):
    gem_img = tf.expand_dims(keras.utils.img_to_array(gen.generate_gem_img(img)), 0)
    letter_img = tf.expand_dims(keras.utils.img_to_array(img), 0)

    # based on letter image, figures out whether there is double points,
    # location of dl, location of tl,
    # the letter, and whether there is a gem
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
    grid_img = gen.get_grid(img)
    players_img = img.crop((370, 0, 540, 499)) # TODO: height needs adjustment for 4 players
    letter_imgs = gen.generate_letter_imgs(grid_img)
    # grid_img.show()
    grid = []
    dl_loc = (-1, -1)
    tl_loc = (-1, -1)
    double_loc = (-1, -1)
    letter_imgs_idx = 0
    for i in range(5):
        grid.append([])
        for j in range(5):
            dl, tl, double, gem, ch = parse_letter(letter_imgs[letter_imgs_idx])
            print("GEM", gem)
            # print("CH", ch)
            grid[i].append(letter.Letter(ch))
            grid[i][j].gem = gem

            if dl:
                dl_loc = (i, j)
            if tl:
                tl_loc = (i, j)
            if double:
                double_loc = (i, j)
                
            letter_imgs_idx += 1
        print("-----")
    for player in players:
        player.gems = 4
        player.pts = 10
    
    return grid, 2, 3, double_loc, dl_loc, tl_loc
    