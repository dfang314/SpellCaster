from PIL import Image as im
import os

imgs_path = __file__[:-len("/generate_letter_imgs.py")]
input_imgs_path = imgs_path + "/input_imgs"
input_files = os.listdir(input_imgs_path)

img_count = 0

for input_file in input_files:
    img = im.open(f"{input_imgs_path}/{input_file}")
    img = img.resize((550, 500))
    grid_img = img.crop((20, 90, 335, 405))

    for i in range(5):
        for j in range(5):
            # grid is 315x315, we need to see more than just our letter (just to be safe)
            crop_left = j * 60
            crop_right = crop_left + 74
            crop_top = i * 60
            crop_bot = crop_top + 74
            letter_img = grid_img.crop((crop_left, crop_top, crop_right, crop_bot))
            letter_img.save(imgs_path + f"/letter_imgs/{img_count}.png")
            img_count += 1