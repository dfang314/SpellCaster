from PIL import Image as im
import os

imgs_path = __file__[:-len("/generate_gem_imgs.py")]
letter_imgs_path = imgs_path + "/letter_imgs"
input_files = os.listdir(letter_imgs_path)

img_count = 0

for input_file in input_files:
    img = im.open(f"{letter_imgs_path}/{input_file}")
    # letter images are 70x70
    gem_img = img.crop((0, 35, 35, 70))
    gem_img.save(imgs_path + f"/gem_imgs/{img_count}.png")
    img_count += 1