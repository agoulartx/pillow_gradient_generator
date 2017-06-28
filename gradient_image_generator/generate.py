from PIL import Image, ImageDraw
from .pallet_picker import pallet_picker
import random

PALLET_ID = random.randrange(1, 11)


def save(obj, id_):
    obj.save(f'gradient_generator_{id_}.png', 'PNG')


def calculate_range(width):
    final_color, initial_color = pallet_picker(PALLET_ID)
    r, g, b = final_color
    dr, dg, db = [(x - y) / width for x, y in zip(initial_color, final_color)]
    return r, g, b, dr, dg, db


def generate_image(width, height):
    img_ = Image.new("RGB", (width, height))
    return img_


def fill_image(img_, width, height):
    draw = ImageDraw.Draw(img_)

    r, g, b, dr, dg, db = calculate_range(width)

    for pixel in range(width):
        r, g, b = r+dr, g+dg, b+db
        draw.line((pixel, 0, pixel, height), fill=(int(r), int(g), int(b)))

if __name__ == "__main__":
    img = generate_image(350, 150)
    print(type(img))
    fill_image(img, 350,150)
    print(type(img))
    save(img, PALLET_ID)



