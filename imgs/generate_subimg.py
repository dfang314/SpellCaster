from PIL import Image as im
import os

def generate_letter_imgs(input_img):
    img = input_img.resize((550, 500))
    grid_img = img.crop((20, 90, 335, 405))

    letter_imgs = []
    for i in range(5):
        for j in range(5):
            # grid is 315x315, we need to see more than just our letter (just to be safe)
            crop_left = j * 60
            crop_right = crop_left + 74
            crop_top = i * 60
            crop_bot = crop_top + 74
            letter_img = grid_img.crop((crop_left, crop_top, crop_right, crop_bot))
            letter_imgs.append(letter_img)
            # letter_img.save(output_path + f"/{img_count}.png")
    return letter_imgs

def generate_gem_img(letter_img):
    # letter images are 74x74
    return letter_img.crop((0, 35, 35, 70))

def save_imgs(imgs, path):
    for i, img in enumerate(imgs):
        img.save(path + f"/{i}.png")

def generate_and_save_all_subimgs():
    imgs_path = __file__[:-len("/generate_subimg.py")]
    input_imgs_path = imgs_path + "/input_imgs"
    input_files = os.listdir(input_imgs_path)

    for input_file in input_files:
        img = im.open(f"{input_imgs_path}/{input_file}")

        letter_imgs = generate_letter_imgs(img)
        gem_imgs = [generate_gem_img(letter_img) for letter_img in letter_imgs]

        save_imgs(letter_imgs, imgs_path + "/letter_imgs")
        save_imgs(gem_imgs, imgs_path + "/gem_imgs")

